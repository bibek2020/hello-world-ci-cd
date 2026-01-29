import unittest
from unittest import TestCase

from app import hello_world


class Test(TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(),"Hello World!")

if __name__ == '__main__':
    unittest.main()
