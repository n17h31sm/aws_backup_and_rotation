import subprocess
import json


#Cleaning images from yesterday
images_clean = {}
with open('/home/backup_rotation/yesterdays_ids.json','r') as imgclean:
    for line in imgclean:
        images_clean = json.loads(line)



for record in list(images_clean):
    subprocess.call(['/usr/local/bin/aws', 'ec2', 'deregister-image', '--image-id', record])

subprocess.call(['rm', '-rf', '/home/backup_rotation/yesterdays_ids.json'])
