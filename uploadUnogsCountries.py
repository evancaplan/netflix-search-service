# handler.py
import boto3
import json
import requests

from lib import http
from lib import secret

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    url = "https://unogsng.p.rapidapi.com/countries"
    headers = {
        "x-rapidapi-host": "unogsng.p.rapidapi.com",
        "x-rapidapi-key": secret.get_rapid_api_key(),
    }

    data = http.get(url, headers)

    # Define table
    table = dynamodb.Table('UnogsCountry')

    # Iterate through countries and add to DynamoDB
    for country in data['results']:
        item = {
            'Id': str(country['id']),
            'Name': country['country'],
            'Code': country['countrycode']
        }
        table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps('Countries added to DynamoDB')
    }
