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

import boto3
import click
from bucket import BucketManager

#SESSION = boto3.Session(profile_name='pythonAutomation')
# S3 = SESSION.resource('s3')
#bucket_manager = BucketManager(SESSION)

SESSION = None
bucket_manager = None

# groups the different functions
# declarator
# @click.option('--profile', default=1,help="Use a given AWS profile.")
@click.group()
@click.option('--profile', default=None, help = "Use a given AWS profile.")
#@click.pass_context
def cli(profile):
    """Webotron deploys websites to AWS."""
    global SESSION, bucket_manager
    session_cfg = {}
    if profile:
        session_cfg['profile_name']=profile

    SESSION = boto3.Session(**session_cfg) #** unwrap the dictoronalr as a paratmer to function
    bucket_manager = BucketManager(SESSION)

# ensures the command line arguments matches with number of function parameters
# click module ensures there is help available for this script --help
@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an S3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 buckets."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
