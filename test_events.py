import unittest
from events import *
from event_manager import *

def do_nothing(data):
    pass

class TestEvents(unittest.TestCase):

    def testFailTrigger(self):
        self.assertEqual(EventManager.triggerEvent(TextEventType("REQUEST","BY_THE_POWER_OF_GRAYSKULL")),False)
        EventManager.subscribe("USER_MESSAGE",do_nothing,TextEventType)
        self.assertEqual(EventManager.triggerEvent(UserUpdateEventType("USER_MESSAGE","BY_THE_POWER_OF_GRAYSKULL")),False)
    
    def testTrigger(self):
        EventManager.subscribe("USER_MESSAGE",do_nothing,UserUpdateEventType)
        self.assertEqual(EventManager.triggerEvent(UserUpdateEventType("USER_MESSAGE","BY_THE_POWER_OF_GRAYSKULL")),False)

if __name__ == '__main__':
    unittest.main()

