# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation');
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)

new_bucket = s3.create_bucket(Bucket='automating-aws-python')
get_ipython().run_line_magic('history', '')
for bucket in s3.buckets.all():
    print(bucket)

ec2_client = session.client('ec2')
ec2_client.all
get_ipython().run_line_magic('save', 'ipythonsession.py 1-20')


import boto3
session = boto3.Session(profile_name='pythonAutomation');
s3 = session.resource('s3')
s3
new_bucket = s3.create_bucket(Bucket='automating-aws-python')
I-search
session.region_name
cat ~/.aws/config
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={ContentType': 'text/html'})
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={ContentType': 'text/html'})
new_bucket.upload_file('index.html', 'index1.html', ExtraArgs={ContentType': 'text/html'})
new_bucket.upload_file('index1.html', 'index1.html', ExtraArgs={ContentType': 'text/html'})
new_bucket
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'})
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
                "arn:aws:s3:::example.com/*"
            ]
        }
    ]
}
"""
policy
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
""" % new_bucket.name
policy
pol = new_bucket.Policy()
pol.put(Policy=policy)
policy
policy = policy.strip()
policy
pol.put(Policy=policy)
ws = new_bucket.Website()
ws.put(WebsiteConfiguration={
'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }})
%save ipythonsession1.py
save ipythonsession1.py
url = "https://%s.s3-website.us-east-1.amazonaws.com" % new_bucket.name
url
url = "http://%s.s3-website.us-east-1.amazonaws.com" % new_bucket.name
url
%history


from pathlib import Path
ls
pathname = "kitten_web"
path = Path(pathname)
path
path.resolve()
list(path.iterdir())
ls kitten_web/
path.is_dir()
path.is_file()
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)


def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
/
z
\
/
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p.as_posix())
handle_directory(path)
pathname = "kitten_web"
path = Path(pathname)
history
from pathlib import Path
ls
pathname = "kitten_web"
path = Path(pathname)
path
path.resolve()
list(path.iterdir())
from pathlib import Path
pathname = "kitten_web"
path = Path(pathname)
path.resolve()
handle_directory(path)
handle_directory(path)
handle_directory(path)
handle_directory(path)
handle_directory(path)
handle_directory(path)
handle_directory(path)
pathname = "~/code/automating-aws-with-python/01-webotron/kitten_web/"
path = Path(pathname)
path.expanduser()
handle_directory(path.expanduser())
pathname = "~/Downloads/Devops/Python/code/automating-aws-with-python/01-webotron/kitten_web/"
path = Path(pathname)
path.expanduser()
handle_directory(path.expanduser())
path
root = pathname
path.relative_to(root)
path.relative_to(root)
root
path
path.relative_to(root)
pwd
root = "/Users/rpokkula/Downloads/Devops/Python/code/automating-aws-with-python/01-webotron/kitten_web/"
path.relative_to(root)
path
root
path = Path(pathname)
path
pathname = '/Users/rpokkula/Downloads/Devops/Python/code/automating-aws-with-python/01-webotron/kitten_web/'
path = Path(pathname)
path
path.relative_to(root)
root = '/Users/rpokkula/Downloads/Devops/Python/code/automating-aws-with-python/01-webotron/kitten_web/
pathname = '/Users/rpokkula/Downloads/Devops/Python/code/automating-aws-with-python/01-webotron/kitten_web/images/Maine_coon_kitten_roarie.jpg'
path = Path(pathname)
path
root
path.relative_to(root)
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p.as_posix()
        )
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print("path: {}§n Key: {}".format(p, p.relative_to(root)))
handle_directory(Path(root))
%history


from collections import namedtuple
Endpoint = namedtyple('Endpoint', ['name','host','zone'])
Endpoint = namedtuple('Endpoint', ['name','host','zone'])
Endpoint
type(Endpoint)
ep1 = Endpoint ('US East (Ohio)', 's3-website.us-east-2.amazonaws.com','Z2O1EMRO9K5GLX')
ep1
ep1.name
ep1.host
ep1.zone
%history


from pprint import print
from pprint import pprint
s3
import boto3
session = boto3.Session(profile_name='pythonAutomation');
s3 = session.resource('s3')
s3
paginator = s3.meta.client.get_paginator('list_objects_v2')
paginatortor
paginator
for page in paginator.paginate(Bucket='automating-aws-python2'):
    for obj in page.get('Contents',[]):
        pprint(obj)
