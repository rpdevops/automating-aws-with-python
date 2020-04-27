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



import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource ('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path,'w') as key_file:
    key_file.write(key.key_material)
ls -l python_automation_key.pem
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ls -l python_automation_key.pem
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-0915e09cc7ceee3ab')
img.name
ec2_apse2 = session.resource('ec2', region_name = 'ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-0915e09cc7ceee3ab')
img_apse2
img_apse2.name
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20200318.2-x86_64-gp2'
filters = [{'Name':'name','Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'],Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'],Filters=filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, instanceType='t2.micro', KeyName=key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, instanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instnaces.name
instnaces.ami_name
instances.name
instances.ami_name
instances
ec2.Instance(id='i-0869148c1d5e18827')
inst = instances[0]
inst.terminates()
inst.terminate()
instances
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances [0]
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
instances
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
 history

  inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId']

)
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'31.54.45.93/32'}]}])
inst.public_dns_name
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}])
history
