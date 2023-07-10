import psycopg2
import json
import boto3
import os

def handler(event,context):
    call_pt_svc()
# """     
# patient creation:
# will need the mahler id 
# add to mahler_id_cx
# then will need to create a master id
# call mstr_intake_mahler 
# will need to update patient in mahler with master_id
# this shouldnt happen
# """
# '''
# update patient
# just need master id
# call mstr_intake_mahler
# '''
# '''
# event creation
# will need event id
# add to mahler_event table (cant remember name)
# call mstr_intake_mahler
# this shouldnt happen
# '''


ssm = boto3.client('ssm',  aws_access_key_id=os.environ['KEY'], aws_secret_access_key=os.environ['SECRET'],  region_name='us-east-2')
param = ssm.get_parameter(Name='uck-etl-db-prod-masterdata', WithDecryption=True )
db_request = json.loads(param['Parameter']['Value']) 

def masterdata_conn():
    hostname = db_request['host']
    portno = db_request['port']
    dbname = db_request['database']
    dbusername = db_request['user']
    dbpassword = db_request['password']
    conn = psycopg2.connect(host=hostname,user=dbusername,port=portno,password=dbpassword,dbname=dbname)
    conn.autocommit = False
    return conn

def call_pt_svc():
    print('hello from api gateway')
