from kdr2net.tests import *

class TestFeedsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='feeds', action='index'))
        # Test response...
