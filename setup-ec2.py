import boto3
import dotenv

# get secure environment variables for keys

config = dotenv.dotenv_values(".env")
print(config)

# function for connecting to EC2
# dont need to put in keys since aws CLI configured\
ec2_client = boto3.client("ec2", region_name="us-east-2")
ec2 = boto3.resource('ec2', region_name="us-east-2")

# instances = ec2.create_instances(
#     ImageId="ami-01107263728f3bef4",
#     MinCount=4,
#     MaxCount=4,
#     InstanceType="t2.micro"
# )

# request EC2 instances
instanceArray = []
for inst in ec2.instances.all():
    print("instance ID: ", inst.id, end="")
    print("instance STATE: ", inst.state["Name"])

    if inst.state["Name"] == "stopped":
        pass
    instanceArray.append(inst.id)

print(instanceArray)
print("\n")
# terminate instances
response = ec2_client.terminate_instances(
    InstanceIds=instanceArray,
)


# monitor existing ec2 instance
# if config.MONITOR == 'ON':
#     response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
# else:
#     response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
