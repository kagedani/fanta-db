from src import initialize
from src.utils.request_utils import send_request, download_request_setup
from src.utils.conversion_utils import from_download_to_players_stats
from src.data.PlayersStats import PlayersStats
import logging
import polars as pl
import json


def start_execution(config):
    login_endpoint = f"{config.FANTACALCIO_IT_ENDPOINT}{config.FANTACALCIO_IT_LOGIN_PATH}"
    body = json.dumps({
      "username": f"{config.USERNAME}",
      "password": f"{config.PSW}"
    })
    headers = {
        "Content-Type": "application/json"
    }

    logging.info(f"Sending request to {login_endpoint} with body {body} and headers {headers}")
    try:
        login_response = send_request("POST", login_endpoint, headers, None, body)
    except Exception:
        lougout_endpoint = f"{config.FANTACALCIO_IT_ENDPOINT}{config.FANTACALCIO_IT_LOGOUT_PATH}"
        logout_response = send_request("POST", lougout_endpoint, headers, None, body)
        logging.info(f"Logout complete for user {config.USERNAME}", extra={"additional_detail": logout_response.status_code})
        raise
    logging.info("🚀 Logged in!")
    login_cookies = login_response.cookies.get_dict()
    cookie_string = ''
    for k in login_cookies:
        cookie_string += f"{k}={login_cookies.get(k)}; "
    logging.debug(f"Cookie received: {cookie_string[:len(cookie_string) - 2]}")

    for season, season_code in config.FANTACALCIO_IT_DOWNLOAD_CONFIG.items():

        download_headers, download_endpoint = download_request_setup(config, cookie_string, season_code)
        logging.info(f"Sending request to {download_endpoint} to download season {season}")
        download_response = send_request("GET", download_endpoint, download_headers, None, config.EMPTY_STRING)

        logging.debug(f"Download result status code: {download_response.status_code}")
        season_file_name = f"src/files/season{season}.xlsx"
        open(season_file_name, "wb").write(download_response.content)
        df = pl.read_excel(
            source=season_file_name,
            sheet_id=1,
            xlsx2csv_options={"skip_empty_lines": True, "truncate_ragged_lines": True},
            read_csv_options={"has_header": True, "skip_rows": 1}
        )
        sql_records = df.to_dicts()
        players_stats = from_download_to_players_stats(sql_records, season)
        logging.info(f"Bulk load for season {season}")
        PlayersStats.bulk_insert(config, players_stats)
        logging.info(f"Bulk load for season {season} - COMPLETED")


if __name__ == "__main__":
    conf = initialize()
    start_execution(conf)
