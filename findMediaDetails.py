import boto3

from lib import http
from lib import secret

rapid_api_url = "https://unogsng.p.rapidapi.com"


def lambda_handler(event, context):
    return get_details_for(event['id'])


def get_details_for(id):
    params = {"netflixid": id}

    headers = {"X-RapidAPI-Key": secret.get_rapid_api_key(), "X-RapidAPI-Host": "unogsng.p.rapidapi.com"}

    details_json = http.get_with_params(rapid_api_url + "/title", params, headers)

    return {
        'statusCode': 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true,
            'Access-Control-Allow-Methods': 'POST,OPTIONS',
        },
        'body': {'details': details_json}
    }
