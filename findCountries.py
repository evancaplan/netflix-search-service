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
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true,
            'Access-Control-Allow-Methods': 'GET,OPTIONS',
        },
        'body': json.dumps(countries)
    }
