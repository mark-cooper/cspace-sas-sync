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
                'impTimout': config.get('imp_timout', '3600'),
                'forceSync': config.get('force_sync', 'true'),
            },
        }

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
            auth=(self.config['username'], self.config['password']),
            timeout=300
        )
        return response


def handler(event, context):
    cspace_sync_event = CollectionSpaceSyncEvent(event)
    response = cspace_sync_event.sync()
    status = {
        'status_code': response.status_code,
        'url': response.url,
        'data': response.text,
    }
    if response.ok:
        logger.info(json.dumps(status))
    else:
        logger.error(json.dumps(status))
    return status
