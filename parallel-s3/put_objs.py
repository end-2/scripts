import string
import random
import boto3
from botocore.exceptions import ClientError
import concurrent.futures

access_key = ''
secret_key = ''
custom_endpoint_url = 'http://localhost:9000'
s3 = boto3.client('s3', 
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key,
    endpoint_url=custom_endpoint_url)

bucket_name = 'test-bucket'

characters = string.ascii_letters + string.digits

def put_objects(num_objects):
    errors = []
    for _ in range(num_objects):
        selected_chars = ''.join(random.choices(characters, k=10))
        try:
            s3.put_object(Bucket=bucket_name, Key=selected_chars, Body=b'')
        except ClientError as e:
            errors += e
    return errors

# create thread pool
with concurrent.futures.ThreadPoolExecutor() as executor:
    # create futures for each character
    futures = [executor.submit(put_objects, 10) for _ in range(1)]

# collect results from all futures
errors = []
for future in concurrent.futures.as_completed(futures):
    res = future.result()
    if res is not None:
        errors += future.result()

print("Error count : ", len(errors))
