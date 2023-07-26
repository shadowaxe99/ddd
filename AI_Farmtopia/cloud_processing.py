```python
import boto3
from botocore.exceptions import NoCredentialsError

class CloudProcessing:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_to_cloud(self, file_name, bucket):
        try:
            self.s3.upload_file(file_name, bucket, file_name)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_from_cloud(self, file_name, bucket):
        try:
            self.s3.download_file(bucket, file_name, file_name)
            print("Download Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

cloud_processing = CloudProcessing()

# Example usage:
# cloud_processing.upload_to_cloud('playerData.json', 'ai-farmtopia-bucket')
# cloud_processing.download_from_cloud('playerData.json', 'ai-farmtopia-bucket')
```