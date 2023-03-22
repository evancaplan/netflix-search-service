import boto3
import json

from lib import http
from lib import secret

rapid_api_url = "https://unogsng.p.rapidapi.com"


def lambda_handler(event, context):
    return get_media_for(event)


def get_media_for(event):
    params = {"orderby": "rating", "limit": event['rows'],
              "countrylist": event['countryOne'] + "," + event['countryTwo'], "country_andorunique": "and",
              "offset": event['offset'], "type": event['mediaType']}

    headers = {"X-RapidAPI-Key": secret.get_rapid_api_key(), "X-RapidAPI-Host": "unogsng.p.rapidapi.com"}

    media_json = http.get_with_params(rapid_api_url + "/search", params, headers)

    return {
        'statusCode': 200,

        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true,
        },
        'body': {'media': media_json['results'], 'total': media_json['total']}
    }
