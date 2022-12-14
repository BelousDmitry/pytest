import os
import pytest
import comp630 
import boto3
from moto import mock_s3

# test bucket specific to class and person
TEST_BUCKET = "test"
TEST_FILE = "bilous.moto.txt"
ENDPOINT_URL = 'http://127.0.0.1:4566'
AWS_PROFILE = 'default'
AWS_REGION = 'us-east-1'

@mock_s3
def test_upload():
    # make scope global
    global TEST_BUCKET
    global TEST_FILE
    # With the moto library imported, the boto3 s3 is fake
    boto3.setup_default_session(profile_name=AWS_PROFILE)
    s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    s3_client.create_bucket(Bucket=TEST_BUCKET)
    with open(TEST_FILE, "rb") as f:
        object_name = os.path.basename(f.name)
        comp630.to_the_cloud(f.name, TEST_BUCKET, s3_client)

    assert True
