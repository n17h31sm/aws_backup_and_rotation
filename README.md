# aws_backup_and_rotation
This are series of scripts that take care of backing up aws ec2 images, moving them to another location and making their rotation. The script uses AWS cli.

The image creation and moving script should be on a seperate host from the backup rotation and cleaning. That is due to AWS cli restrictions on zones, you can't use more than one zone at a time on a single host.

Example cronjobs:

1 ZONE HOST:
0 8 * * * back_up_aws_move.py
0 9 * * * move_aws_image.py
0 10 * * * cleanup.py

2 ZONE HOST (where you move images to):

0 6 * 3 * backup_rotation.py
0 7 * * * clean_yesterdays_image.py
