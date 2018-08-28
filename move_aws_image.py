import json
import subprocess

# Open the file with the new ids, and move each one to another zone
ids_name = {}
with open('/home/backup/new_ids.json','r') as newid:
        for line in newid:
            ids_name = json.loads(line)

#dictionary of the ids of the move images
yesterdays_images = {}

for record in list(ids_name):
    image_id = json.loads(subprocess.check_output(['/usr/local/bin/aws', 'ec2', 'copy-image', '--source-image-id', record, '--source-region', 'eu-west-x', '--region', 'us-west-x', '--name', ids_name[record]]))
    yesterdays_images[image_id['ImageId']] = ids_name[record]

# Put the new ids for the images copied over to the new zone
with open('/home/yesterdays_ids.json','w') as yesid:
         yesid.write(json.dumps(yesterdays_images))
