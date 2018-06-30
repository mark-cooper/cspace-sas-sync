import unittest

from sas.sync import CollectionSpaceSyncEvent


class CollectionSpaceSyncEventTestCase(unittest.TestCase):

    config = {
        'services_url': 'https://core.collectionspace.org/cspace-services',
        'authtype': 'vocabularies',
        'refname': 'urn:cspace:name(materialuse)',
        'username': 'admin@core.collectionspace.org',
        'password': 'Administrator',
    }
    sync_url = 'https://core.collectionspace.org/cspace-services/vocabularies/urn:cspace:name(materialuse)/sync'

    def test_should_return_expected_build_url(self):
        cspace_sync_event = CollectionSpaceSyncEvent(self.config)
        self.assertEqual(
            cspace_sync_event.build_url(),
            self.sync_url
        )


if __name__ == '__main__':
    unittest.main()
