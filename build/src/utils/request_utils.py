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
        response = {'error': response.reason, 'message': response.text}
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'ConnectionError: error during the connection to {url}, '
                      f'the timeout is set to {MAX_CONNECT_TIMEOUT}')
        response = {'error': errc}
    except requests.exceptions.RequestException as err:
        logging.error(f'RequestException {err}')
        response = {'error': err}

    return response


def download_request_setup(conf, cookies, season_code):
    headers = {
        'Cookie': cookies
    }
    endpoint = f"{conf.FANTACALCIO_IT_ENDPOINT}{conf.FANTACALCIO_IT_DOWNLOAD_PATH}"
    endpoint = endpoint.replace("{SEASON}", season_code)

    return headers, endpoint
