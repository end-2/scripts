import string
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
prefix = ''

characters = string.ascii_letters + string.digits

def list_objects(prefix, object_keys, continuation_token=None):
    if continuation_token is not None:
        objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, ContinuationToken=continuation_token)
    else:
        objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    if 'Contents' in objects:
        object_keys += [obj['Key'] for obj in objects['Contents']]
    if 'NextContinuationToken' in objects:
        next_continuation_token = objects['NextContinuationToken']
        list_objects(prefix, object_keys, next_continuation_token)

    for key in object_keys:
        try:
            s3.delete_object(Bucket=bucket_name, Key=key)
        except ClientError as e:
            print(f'Error uploading object: {e}')

    return object_keys

# create thread pool
with concurrent.futures.ThreadPoolExecutor() as executor:
    # create futures for each character
    futures = [executor.submit(list_objects, prefix + character, []) for character in characters]

# collect results from all futures
results = []
for future in concurrent.futures.as_completed(futures):
    res = future.result()
    if res is not None:
        results += future.result()

print("Deleted object count: ", len(results))
