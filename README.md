# File-Upload-in-S3-Bucket

**Step 1: Set Up Your Environment**

Create an S3 bucket:
Go to the AWS Management Console.
Navigate to S3 and create a bucket (e.g., my-document-storage-bucket).

Create an IAM Role:
Go to the IAM Management Console.
Create a role with AWSLambdaBasicExecutionRole and S3 full access permissions.

Set up AWS CLI :
Install and configure the AWS CLI to interact with AWS services via the terminal.

**Step 2: Write the Lambda Function**
program file is File-Upload-in-S3-Bucket.py 

**Step 3: Deploy the Function**

1. Create a Deployment Package:
Package your Python script and its dependencies into a .zip file.
For example: zip function.zip File-Upload-in-S3-Bucket.py

2. Deploy the Lambda Function:
Use the AWS Management Console:
Create a new Lambda function.
Upload the .zip file as the function code.
Set the runtime to Python.
Configure the handler as lambda_function.lambda_handler.
Attach the IAM role created earlier.

Set the environment variable for the bucket name:
Key: BUCKET_NAME
Value: my-document-storage-bucket

**Step 4: Test the Lambda Function**

Create a Test Event: Use the following example test payload in the Lambda console:
e.g: {
    "isBase64Encoded": false,
    "body": "Sample content for a PDF or document",
    "headers": {
        "filename": "example.pdf"
    }
}

Run the Function:
Execute the function from the console and verify that the file is uploaded to your S3 bucket.

**Step 5: Verify the File in S3**

Go to the S3 bucket in the AWS Management Console and check that the file (example.pdf) exists.

