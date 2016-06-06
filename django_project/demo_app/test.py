__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '06/06/16'

from django.test import TestCase


class TestHouseCreation(TestCase):

    def setUp(self):
        """Run this before each of the tests below"""
        pass

    def tearDown(self):
        """Run this after each of the tests below"""
        pass

    def test_house_created(self):
        self.assertNotEqual(2, 3)