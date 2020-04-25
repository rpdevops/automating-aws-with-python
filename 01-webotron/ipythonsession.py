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
