import logging
import boto3
from botocore.exceptions import ClientError



def to_the_cloud(file_name, bucket, client, object_name=None,):
    
    if object_name is None:
        object_name = file_name

    try:
        response = client.upload_file(file_name, bucket, object_name)
        print(f'Upload Response: {response}')
    except ClientError as e:
        logging.error(e)
        return False
    
    return True
