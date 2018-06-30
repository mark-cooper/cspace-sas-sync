# cspace-sas-sync

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

Serverless application to schedule CollectionSpace SAS sync.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt

npm install
pytest

sls invoke local -f sync -l -p config/example.json
sls deploy [--aws-profile]
```

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
