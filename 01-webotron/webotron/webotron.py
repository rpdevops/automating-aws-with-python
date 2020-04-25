import boto3
import click

session = boto3.Session(profile_name='pythonAutomation');
s3 = session.resource('s3')

#groups the different functions
#declarator
#@click.option('--profile', default=1,help="Use a given AWS profile.")
@click.group()
@click.pass_context
def cli(bucket):
    "Webotron deploys websites to AWS"
    pass

# ensures the command line arguments matches with number of function parameters
#click module ensures there is help available for this script --help
@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
