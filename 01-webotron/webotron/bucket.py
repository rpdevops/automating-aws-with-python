# -*- coding: utf-8  -*-

"""Classes for S3 Buckets."""

from pathlib import Path
import mimetypes
# from mimetypes import guess_type

from botocore.exceptions import ClientError


class BucketManager:
    """Manage an S3 bucket."""

    def __init__(self, session):
        """Create a BucketManager Object."""
        self.session = session
        self.s3 = session.resource('s3')

    def all_buckets(self):
        """List all buckets."""
        return self.s3.buckets.all()

    def all_objects(self, bucket_name):
        """List all Object in a bucket."""
        return self.s3.Bucket(bucket_name).objects.all()

    def init_bucket(self, bucket_name):
        """Initialize bucket."""
        s3_bucket = None
        try:
            s3_bucket = self.s3.create_bucket(Bucket=bucket_name)
        except ClientError as error:
            # print(e.response)
            if error.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                s3_bucket = self.s3.Bucket(bucket_name)
            else:
                raise error

        return s3_bucket

    def set_policy(self, bucket):
        """Set policy for the bucket."""
        policy = """
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": [
                        "s3:GetObject"
                    ],
                    "Resource": [
                        "arn:aws:s3:::%s/*"
                    ]
                }
            ]
        }
        """ % bucket.name
        policy = policy.strip()

        pol = bucket.Policy()
        pol.put(Policy=policy)

    def configure_website(self, bucket):
        """Configure Website."""
        # ws = s3_bucket.Website()
        bucket.Website().put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }})

    @staticmethod
    def upload_file(bucket, path, key):
        """Upload path to s3_bucket at S3."""
        content_type = mimetypes.guess_type(key)[0] or 'text/plain'

        return bucket.upload_file(
            path, key, ExtraArgs={'ContentType': content_type})

    def sync(self, pathname, bucket_name):
        """Sync objects to S3 Bucket."""
        bucket = self.s3.Bucket(bucket_name)

        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):
            for p in target.iterdir():
                if p.is_dir():
                    handle_directory(p)
                if p.is_file():
                    # print("path: {}§n Key: {}".
                    # format(p, p.relative_to(root)))
                    self.upload_file(bucket, str(p),
                                     str(p.relative_to(root)))

        handle_directory(root)
