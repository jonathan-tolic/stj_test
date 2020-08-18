import abc

class EventType:
    """Abstract Event Type used to enforce all children have sanity checks"""
    
    @abc.abstractmethod    
    def sanityCheck(self):
        """check if event data is sane, return boolean"""
        
        return False

class UserUpdateEventType(EventType):
    """User update event that adds new UI debug line"""
    
    class UserUpateData:
        """Data contained in event"""    
    #NOTE: since the subscribers should not really be aware that there is an event pattern, this would be better situated with them
        
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
    """Text Event type""" 
    
    def __init__(self,event,text):
        self.event = event
        self.event_data = str(text)
        
    def sanityCheck(self):
        """sanity check. The constructor in this case guarantees sanity"""
        
        return True
    
