#!/usr/bin/env python

#'''Farmware: execute a Send Message command.'''

import os
import json
import requests

def log(message, message_type):
    'Send a send_message command to post a log to the Web App.'
    requests.post(
        os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
        headers={'Authorization': 'Bearer ' + os.environ['FARMWARE_TOKEN'],
                 'content-type': 'application/json'},
        data=json.dumps({
            'kind': 'send_message',
            'args': {
                'message': message,
                'message_type': message_type}}))

if __name__ == '__main__':
    log('Hello World!', 'success')
