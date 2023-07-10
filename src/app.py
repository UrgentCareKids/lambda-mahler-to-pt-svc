import psycopg2
import json
import boto3
import os

def handler(event,context):
    payload = json.loads(event['body'])
    
    # Call the function to update your internal database
    call_pt_svc(payload)


    # Return a successful response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': 'Update successful'})
    }

# ssm = boto3.client('ssm',  aws_access_key_id=os.environ['KEY'], aws_secret_access_key=os.environ['SECRET'],  region_name='us-east-2')
# param = ssm.get_parameter(Name='uck-etl-db-prod-masterdata', WithDecryption=True )
# db_request = json.loads(param['Parameter']['Value']) 

# def masterdata_conn():
#     hostname = db_request['host']
#     portno = db_request['port']
#     dbname = db_request['database']
#     dbusername = db_request['user']
#     dbpassword = db_request['password']
#     conn = psycopg2.connect(host=hostname,user=dbusername,port=portno,password=dbpassword,dbname=dbname)
#     conn.autocommit = False
#     return conn

def call_pt_svc(payload):
    print('hello from api gateway: ', payload)
