import requests
import logging
import urllib3

MAX_CONNECT_TIMEOUT = 30
MAX_RESPONSE_TIMEOUT = 30


def send_request(method, url, headers, params, payload):
    response = {}
    urllib3.disable_warnings()
    try:
        if method == 'POST':
            response = requests.post(url, headers=headers,
                                     params=params, data=payload,
                                     verify=False, timeout=(MAX_CONNECT_TIMEOUT, MAX_RESPONSE_TIMEOUT))
        if method == 'GET':
            response = requests.get(url, headers=headers,
                                    params=params, data=payload,
                                    verify=False, timeout=(MAX_CONNECT_TIMEOUT, MAX_RESPONSE_TIMEOUT))
    except requests.exceptions.HTTPError as errh:
        logging.error(f'HTTPError {response.status_code}, {errh}')
        logging.error(f'Body: {response.text}')
        raise
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'ConnectionError: error during the connection to {url}, '
                      f'the timeout is set to {MAX_CONNECT_TIMEOUT}')
        raise
    except requests.exceptions.RequestException as err:
        logging.error(f'RequestException {err}')
        raise
    if response.status_code != 200 or response.status_code != 201:
        raise RuntimeError(f"Failed request with status {response.status_code}: {response.reason}")
    return response


def download_request_setup(conf, cookies, season_code):
    headers = {
        'Cookie': cookies
    }
    endpoint = f"{conf.FANTACALCIO_IT_ENDPOINT}{conf.FANTACALCIO_IT_DOWNLOAD_PATH}"
    endpoint = endpoint.replace("{SEASON}", season_code)

    return headers, endpoint
