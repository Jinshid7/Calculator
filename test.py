#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_intro(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'This is an arithmetic calculator\n')

    def test_square(self):
        a='7'
        rv = self.app.get(f'/square/{a}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'49\n')

    def test_cube(self):
        b=5
        rv = self.app.get(f'/cube/{b}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'125\n')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
