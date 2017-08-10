import unittest

from app.modules.sample_module import SampleModule


class TestSampleModule(unittest.TestCase):
    def test_sample_module(self):
        obj = SampleModule()
        actual = obj.sample('test')
        self.assertTrue('test test', actual)
        self.assertTrue(True)
