import json
import boto3
import base64
import os

def lambda_handler(event, context):
    """
    AWS Lambda function to store a document or PDF file in an S3 bucket.

    :param event: The input event, should contain file content and metadata.
    :param context: AWS Lambda context object.
    """
    # S3 bucket name
    bucket_name = os.environ.get('BUCKET_NAME')  # Store the bucket name in Lambda's environment variables

    # Check if bucket name is configured
    if not bucket_name:
        return {
            'statusCode': 500,
            'body': json.dumps('S3 bucket name is not configured.')
        }

    # Parse input
    try:
        file_content = event['body']  # Assuming the file content is passed in the body
        file_name = event['headers']['filename']  # Filename is passed in the headers

        # Decode Base64 if the content is encoded
        if event['isBase64Encoded']:
            file_content = base64.b64decode(file_content)

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing required field: {e}")
        }

    # Upload to S3
    try:
        s3_client = boto3.client('s3')

        # Upload file to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"File '{file_name}' uploaded successfully to '{bucket_name}'.")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to upload file: {str(e)}")
        }