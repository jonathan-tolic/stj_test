import abc

class EventType:
    @abc.abstractmethod    
    def sanityCheck(self):
        return False

class UserUpdateEventType(EventType):
    class UserUpateData:
        def __init__(self, uu_type, uu_text):
            self.uu_text = str(uu_text)
            self.uu_type = str(uu_type)
        def __str__(self):
            return "{0}:{1}".format(self.uu_type,self.uu_text)
    
    def __init__(self):
        self.event_data = self.__init__("","")
        
    def __init__(self, uu_type, uu_text):
        self.event_data = UserUpdateEventType.UserUpateData(uu_type, uu_text)    
        self.event="USER_MESSAGE"
        
    def sanityCheck(self):
        if isinstance(self.event_data,UserUpdateEventType.UserUpateData):
            return True
        return False

class TextEventType(EventType):
    def __init__(self,event,text):
        self.event = event
        self.event_data = str(text)
        
    def sanityCheck(self):
        return True
    
