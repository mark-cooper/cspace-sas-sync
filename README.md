# cspace-sas-sync

[![Build Status](https://travis-ci.com/mark-cooper/cspace-sas-sync.svg?branch=master)](https://travis-ci.com/mark-cooper/cspace-sas-sync) [![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

Serverless application to schedule CollectionSpace SAS sync.

## Setup

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt

npm install -g serverless
npm install
pytest

sls invoke local -f sync -l -p test/example.json

sls deploy [--config] [--aws-profile]
sls remove [--config] [--aws-profile]
# deploy example with options
sls deploy --config ./config/sync.yml --aws-profile collectionspace
sls remove --config ./config/sync.yml --aws-profile collectionspace
```

## Config

```yml
sync:
  - schedule:
      # 6.30am UTC
      rate: cron(30 6 * * ? *)
      enabled: true
      input:
        services_url: ${ssm:cspace_sas_services_url}
        authtype: $type
        refname: urn:cspace:name($term)
        username: ${ssm:cspace_sas_username~true}
        password: ${ssm:cspace_sas_password~true}
  - schedule:
      # ...
```

The corresponding param store key / value should be created before deploy.

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
