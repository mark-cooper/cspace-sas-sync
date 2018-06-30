import json
import logging
import os
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class CollectionSpaceSyncEvent(object):
    def __init__(self, config):
        self.config = {
            'services_url': config['services_url'],
            'authtype': config['authtype'],
            'refname': config['refname'],
            'username': config['username'],
            'password': config['password'],
            'params': {
                'impTimout': '3600',
                'forceSync': 'true',
            },
        }
        if 'params' in config:
            self.config['params'] = self.config['params'].update(
                config['params']
            )

    def build_url(self):
        self.sync_url = os.path.join(
            self.config['services_url'],
            self.config['authtype'],
            self.config['refname'],
            'sync'
        )
        return self.sync_url

    def sync(self):
        response = requests.post(
            self.build_url(),
            params=self.config['params'],
            auth=(self.config['username'], self.config['password'])
        )
        if not response.ok:
            raise Exception('Sync error: ' + json.dumps(response.json()))
        return response


def handler(event, context):
    cspace_sync_event = CollectionSpaceSyncEvent(event)
    response = cspace_sync_event.sync()
    return {
        'status': 'ok',
        'url': cspace_sync_event.sync_url,
        'data': response.text,
    }
