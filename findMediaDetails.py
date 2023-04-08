import boto3
import traceback
import json

from lib import http
from lib import secret

rapid_api_url = "https://unogsng.p.rapidapi.com"


def lambda_handler(event, context):
    try:
        return get_details_for(event['id'])
    except Exception as e:
        print("Error processing the event: ", str(e))
        print("Traceback: ", traceback.format_exc())
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
            },
            'body': json.dumps({'message': 'Internal server error ' + str(e)})
        }


def get_details_for(id):
    params = {"netflixid": str(id)}

    headers = {"X-RapidAPI-Key": secret.get_rapid_api_key(), "X-RapidAPI-Host": "unogsng.p.rapidapi.com"}

    details_json = http.get_with_params(rapid_api_url + "/title", params, headers)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
        },
        'body': json.dumps(details_json)
    }
