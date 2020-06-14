import boto3
from datetime import date
from datetime import time
from datetime import datetime
import re
from boto3 import client

s3 = boto3.resource('s3')
# aws --profile vaultprod s3 ls s3://wkb-db-backups/wkb-us-west-2-production-ft-mysql/restore-complete-token/ | grep 03-03-2020| awk '{print $4}'
bucket = s3.Bucket('wkb-db-backups')
token = date.today()
print ("Token format", str(token.strftime("%m-,%d,-%Y").replace(',','')))
print ("Today's Date", token.strftime("%m/,%d/,%Y").replace(',',''))

var = 'pankaj.gautam'
print (var)
bucket = 'veevatechops-pubkeys'
prefix = 'ssh-certs/prod/'

client = boto3.client('s3')
def ListFiles(client):
        """List files in S3 bucket"""
        response = client.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter='/')
        for content in response.get('Contents', []):
            yield content.get('Key')
file_list = ListFiles(client)
##    print( 'Restore token found: %s' % file)
for file in file_list:
    if re.search( rf'{var}', file):
       print( 'Restore token found: %s' % file)
