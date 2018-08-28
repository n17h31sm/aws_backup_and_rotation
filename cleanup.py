import json
import subprocess


ids_name = {}
with open('new_ids.json','r') as newid:
    for line in newid:
        ids_name = json.loads(line)


# clean up ireland zone
for record in list(ids_name):
    subprocess.call(['/usr/local/bin/aws', 'ec2', 'deregister-image', '--image-id', record])
