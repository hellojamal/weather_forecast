#! /urs/bin/env python flask
# _*_ coding: utf-8

# project unittest file


import unittest


class MyTestCase(unittest.TestCase):
    """ unittest basic class"""

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
