import boto3

s3 = boto3.client("s3")
BUCKET_NAME = "customer-churn-saad-project"  # your actual bucket

def upload_file(local_path, s3_key):
    s3.upload_file(local_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {local_path} to s3://{BUCKET_NAME}/{s3_key}")

if __name__ == "__main__":
    upload_file("data/raw/dataset.csv", "raw/dataset.csv")
    upload_file("models/my_model.pkl", "models/my_model.pkl")