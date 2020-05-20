import json
import os
import logging

import boto3
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger("handler_logger")
logger.setLevel(logging.DEBUG)

def create(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['datetime'])
    logger.info(table)

    item = {
        'date': "20-05-2020",
        'time': "22:00:00",
    }

    # write the todo to the database
    if event.get('httpMethod') == 'POST':
    table.put_item(Item=item)
	
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
			   }

    return response
