import json
import logging

import requests
from bs4 import BeautifulSoup


def get_title(event, context):
    data = json.loads(event['body'])

    if 'url' not in data:
        message = "URL not provided"
        logging.error(message)
        response = {
            "statusCode": 400,
            "body": message
        }
        return response

    url = data['url']

    try:
        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")
        response = {
            "statusCode": 200,
            "body": f"{soup.title.string}"
        }
        return response
    except requests.RequestException as e:
        logging.exception(f"Exception encountered: {e}")
        response = {
            "statusCode": 500,
            "body": f"{e}"
        }
        return response
