from __future__ import absolute_import

from xml.etree import ElementTree as ET

from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from django_comments.models import Comment

from . import CommentTestCase
from testapp.models import Article


class CommentFeedTests(CommentTestCase):
    urls = 'testapp.urls'
    feed_url = '/rss/comments/'

    def setUp(self):
        pass

    def test_feed(self):
        response = self.client.get(self.feed_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/rss+xml; charset=utf-8')

        rss_elem = ET.fromstring(response.content)

        self.assertEqual(rss_elem.tag, "rss")
        self.assertEqual(rss_elem.attrib, {"version": "2.0"})

        channel_elem = rss_elem.find("channel")
