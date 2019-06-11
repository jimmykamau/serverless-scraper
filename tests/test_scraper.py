import json
import unittest

from scraper.scrap import get_title


class TestScraper(unittest.TestCase):

    def setUp(self):
        self.event = dict()

    def test_get_title(self):
        self.event['body'] = json.dumps(
            {
                'url': "http://example.com/"
            }
        )
        response = get_title(self.event, None)
        self.assertEqual(200, response['statusCode'])
        self.assertEqual("Example Domain", response['body'])


if __name__ == '__main__':
    unittest.main()
