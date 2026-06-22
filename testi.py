import boto3

client =  boto3.client('s3', region_name='us-east-1')

response = client.get_bucket_acl(
    Bucket = 'shauryan-demogod-boto3-prac-341',   
)
print(response)
