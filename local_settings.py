'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC88bbc14a2aa2551d656c847cc2468f95" 
AUTH_TOKEN = "3863e10db5e44f8b1c9f4d28c9715eb2"
BSSSPAM_APP_SID = "APeb17f3f7aa41b2e02cc2ec2ab0611aef"
BSS_SPAM_ID = "+16178302533"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
