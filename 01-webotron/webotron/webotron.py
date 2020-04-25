#!/usr/bin/python What interpreter should be used to run this script
# -*- coding: utf-8 -*-

"""Webotron: Deploy websites with AWS.

Webotron automates the process of deploying static web content_type
- Configre AWS S3 buckets
  - Create them
  - Set them up for static website hosting
  - Deploy local files to them
- Confgire DNS with AWS Route 53
- Congifure a Content Delivery Network and SSL with AWS
"""

from pathlib import Path
import mimetypes
# from mimetypes import guess_type

import boto3
from botocore.exceptions import ClientError

import click

SESSION = boto3.Session(profile_name='pythonAutomation')
S3 = SESSION.resource('s3')

# groups the different functions
# declarator
# @click.option('--profile', default=1,help="Use a given AWS profile.")
@click.group()
@click.pass_context
def cli(bucket):
    """Webotron deploys websites to AWS."""
    pass

# ensures the command line arguments matches with number of function parameters
# click module ensures there is help available for this script --help
@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in S3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an S3 bucket."""
    for obj in S3.Bucket(bucket).objects.all():
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 buckets."""
    s3_bucket = None

    try:
        s3_bucket = S3.create_bucket(Bucket=bucket)
    except ClientError as error:
        # print(e.response)
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = S3.Bucket(bucket)
        else:
            raise error

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
    """ % s3_bucket.name

    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)

    # ws = s3_bucket.Website()
    s3_bucket.Website().put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }})
    return


def upload_file(s3_bucket, path, key):
    """Upload path to s3_bucket at S3."""
    content_type = mimetypes.guess_type(key)[0] or 'text/plain'
    s3_bucket.upload_file(
        path, key, ExtraArgs={'ContentType': content_type})


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    s3_bucket = S3.Bucket(bucket)

    root = Path(pathname).expanduser().resolve()

    def handle_directory(target):
        for p in target.iterdir():
            if p.is_dir():
                handle_directory(p)
            if p.is_file():
                # print("path: {}§n Key: {}".format(p, p.relative_to(root)))
                upload_file(s3_bucket, str(p), str(p.relative_to(root)))
    handle_directory(root)


if __name__ == '__main__':
    cli()
