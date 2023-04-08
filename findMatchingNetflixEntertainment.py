import boto3
import json
import traceback

from lib import http
from lib import secret

rapid_api_url = "https://unogsng.p.rapidapi.com"


def lambda_handler(event, context):
    try:
        return get_media_for(event)
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


def get_media_for(event):
    requested_params = json.loads(event['body'])
    params = {"orderby": "rating", "limit": '50',
              "countrylist": requested_params['countryOne'] + "," + requested_params['countryTwo'],
              "country_andorunique": "and",
              "offset": str(requested_params['offset']), "type": requested_params['mediaType']}

    headers = {"X-RapidAPI-Key": secret.get_rapid_api_key(), "X-RapidAPI-Host": "unogsng.p.rapidapi.com"}

    media_json = http.get_with_params(rapid_api_url + "/search", params, headers)

    if len(media_json['results']) > 0:
        if requested_params['offset'] > 0:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': 'true',
                },
                'body': json.dumps({'media': media_json['results'], 'total': media_json['total']})
            }
        else:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': 'true',
                },
                'body': json.dumps({'media': media_json['results']})
            }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
            },
            'body': json.dumps({'media': [], 'total': '0'})
        }
