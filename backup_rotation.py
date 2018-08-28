import json
import subprocess
import datetime


#Clean the 2 weeks old images
images_del = {}
with open('/home/backup_rotation/last_week2.json','r') as imgdel:
    for line in imgdel:
        images_del = json.loads(line)

for record in list(images_del):
    subprocess.call(['/usr/local/bin/aws', 'ec2', 'deregister-image', '--image-id', record])

#Move 1 week old images to the 2 week old file
subprocess.call(['mv', '/home/backup_rotation/last_week.json', '/home/backup_rotation/last_week2.json'])


now = datetime.datetime.now()

#Copy images from yesterday as weekly ones, before you run the backup script for that day
images_tobck = {}
with open('/home/backup_rotation/yesterdays_ids.json','r') as imgbck:
    for line in imgbck:
        images_tobck = json.loads(line)

last_week = {}

for record in list(images_tobck):
    name_img = str(images_tobck[record] + "week")
    image_id = json.loads(str(subprocess.check_output(['/usr/local/bin/aws', 'ec2', 'copy-image', '--source-image-id', record, '--source-region', 'us-west-x', '--region', 'us-west-x', '--name', name_img])))

    last_week[image_id['ImageId']] = images_tobck[record]

with open('/home/backup_rotation/last_week.json','w') as yesid:
       yesid.write(json.dumps(last_week))
