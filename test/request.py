#!/usr/bin/env python3

import requests
import os

url = os.getenv('URL', 'https://nightly.collectionspace.org/cspace-services/orgauthorities/urn:cspace:name(organization)/sync')
username = os.getenv('USERNAME', 'admin@core.collectionspace.org')
password = os.getenv('PASSWORD', 'Administrator')

response = requests.post(
    url,
    params={'impTimout': '3600', 'forceSync': 'true'},
    auth=(username, password),
    timeout=300
)

print(response.url)
print(response.status_code)
print(response.content)
