import boto3

BUCKET_NAME = "customer-churn-saad-project"  # replace with your actual bucket
LOCAL_FILE =  r"data/raw/dataset.csv"
S3_KEY = "raw/dataset.csv"  # path/filename inside the bucket

s3 = boto3.client("s3")

def upload_file():
    s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
    print(f"Uploaded {LOCAL_FILE} to s3://{BUCKET_NAME}/{S3_KEY}")

if __name__ == "__main__":
    upload_file()