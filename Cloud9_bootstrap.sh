#!/bin/ksh
sudo yum update -y 
sudo pip install --upgrade pip
sudo pip install pipenv boto3 c7n ipython


aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem

aws ec2 describe-vpcs --filters "Name=tag:Name,Values=myhostname"
aws ec2 describe-vpcs --vpc-ids vpc-06e4ab6c6cEXAMPLE

aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e


