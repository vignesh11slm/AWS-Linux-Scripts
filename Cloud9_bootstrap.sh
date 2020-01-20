#!/bin/ksh
sudo yum update -y 
sudo pip install --upgrade pip
sudo pip install pipenv boto3 c7n ipython


aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem

aws ec2 describe-vpcs --filters "Name=tag:Name,Values=myhostname"
aws ec2 describe-vpcs --vpc-ids vpc-06e4ab6c6cEXAMPLE

aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e

DEFAULTVPCID="$(aws ec2 describe-vpcs \
    --filter "Name=isDefault, Values=true" \
    --query "Vpcs[0].VpcId" --output text)"
    
Check this link : http://okigiveup.net/discovering-aws-with-cli-part-1-basics/



DEFAULTVPCID="$(aws ec2 describe-vpcs --filter "Name=isDefault, Values=true" --query "Vpcs[0].VpcId" --output text)"

SUBNETID="$(aws ec2 describe-subnets --filter "Name=vpc-id,Values=$DEFAULTVPCID" --query "Subnets[0].SubnetId" --output text)"

aws ec2 describe-security-groups --filter "Name=vpc-id,Values=$DEFAULTVPCID" "Name=group-name,Values=default" --query "SecurityGroups[0].GroupId" --output text

aws ec2 describe-images --owners amazon --filters 'Name=name,Values=amzn2-ami-hvm-2.0.????????.?-x86_64-gp2' 'Name=state,Values=available' --query 'reverse(sort_by(Images, &CreationDate))[:1].ImageId' --output text
