# retrieve_countries_handler.py
import boto3
import json

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table('UnogsCountry')

    # Scan the table for all countries
    response = table.scan()
    countries = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(countries)
    }
