# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource ('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path,'w') as key_file:
    key_file.write(key.key_material)

get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
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
instances
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
get_ipython().run_line_magic('history', '')
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId']

)
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'31.54.45.93/32'}]}])
inst.public_dns_name
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}])
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ec2_example.py 1-65')
