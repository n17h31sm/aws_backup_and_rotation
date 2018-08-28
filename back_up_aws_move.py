import subprocess
import json
import datetime



#Creating new backups
now = datetime.datetime.now()

# Dictionary of all available instances
instances_dict = {}

# Call aws cli command, and parse json, then put it into instances_dict{}

current_instances = json.loads(subprocess.check_output(['/usr/local/bin/aws', 'ec2', 'describe-instances']))
for line in current_instances['Reservations']:
    instance_id = line['Instances'][0]['InstanceId']
    instance_name = line['Instances'][0]['Tags'][0]['Value']
    instances_dict[instance_id] = instance_name

# dict of the ids and names given to the newly created images
images_dict = {}

# Go over all instances except Kibana and Nagios and make images, putting their ids into  the dictionary
for record in list(instances_dict):
    if instances_dict[record] != 'Kibana' and instances_dict[record] != 'Nagios':
        image_id = json.loads(subprocess.check_output(['/usr/local/bin/aws', 'ec2', 'create-image', '--instance-id', record, '--name', instances_dict[record] + now.strftime('%Y-%m-%d'), '--no-reboot']))
        images_dict[image_id['ImageId']] = instances_dict[record] + now.strftime('%Y-%m-%d')

#Write the new ids to file so they can be moved to the other zone
with open('/home/openvpnas/backup/new_ids.json','w') as ni:
     ni.write(json.dumps(images_dict))
