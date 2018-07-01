import unittest

from sas.sync import CollectionSpaceSyncEvent
from unittest.mock import patch


class CollectionSpaceSyncEventTestCase(unittest.TestCase):

    config = {
        'services_url': 'https://core.collectionspace.org/cspace-services',
        'authtype': 'vocabularies',
        'refname': 'urn:cspace:name(materialuse)',
        'username': 'admin@core.collectionspace.org',
        'password': 'Administrator',
    }
    cspace_sync_event = CollectionSpaceSyncEvent(config)
    sync_url = 'https://core.collectionspace.org/cspace-services/vocabularies/urn:cspace:name(materialuse)/sync' # noqa

    def test_should_return_expected_build_url(self):
        self.assertEqual(
            self.cspace_sync_event.build_url(),
            self.sync_url
        )

    @patch('sas.sync.requests.post')
    def test_should_return_post_sync_event_fail(self, mock_post):
        mock_post.return_value.ok = False
        mock_post.return_value.status_code = 401
        mock_post.return_value.text = 'Sad =('

        response = self.cspace_sync_event.sync()
        self.assertEqual(response.status_code, 401)

    @patch('sas.sync.requests.post')
    def test_should_return_post_sync_event_success(self, mock_post):
        mock_post.return_value.ok = True
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = 'Happy =)'

        response = self.cspace_sync_event.sync()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
