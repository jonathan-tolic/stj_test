import unittest
from events import *
from event_manager import *

def do_nothing(data):
    pass


class TestEvents(unittest.TestCase):
    """Tests trigger if it fails or succeeds based on current subscriptions"""
    def testFailTrigger(self):
        """Should fail due to lack of subscription"""
        self.assertEqual(EventManager.triggerEvent(TextEventType("REQUEST","BY_THE_POWER_OF_GRAYSKULL")),False)
        """Should fail due to wrong event type"""
        EventManager.subscribe("USER_MESSAGE",do_nothing,TextEventType)
        self.assertEqual(EventManager.triggerEvent(UserUpdateEventType("USER_MESSAGE","BY_THE_POWER_OF_GRAYSKULL")),False)
        EventManager.subscriptions = {}
    def testTrigger(self):
        """Should succeed"""
        EventManager.subscribe("USER_MESSAGE",do_nothing,UserUpdateEventType)
        self.assertEqual(EventManager.triggerEvent(UserUpdateEventType("USER_MESSAGE","BY_THE_POWER_OF_GRAYSKULL")),True)

if __name__ == '__main__':
    unittest.main()

