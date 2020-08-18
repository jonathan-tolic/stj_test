class EventManager:
    subscriptions = {}
    errors = []
    def triggerEvent(event):
        success = False
        if not event.sanityCheck():
            print("\033[1;31;40m ERR: {0} event is insane. Data: {1} \033[0m".format(event.event,event.event_data))
            EventManager.errors.append("ERR: {0} event is insane. Data: {1} \033[0m".format(event.event,event.event_data))
            return success
        if event.event in EventManager.subscriptions:
            for sub in EventManager.subscriptions[event.event]:
                if not isinstance(event,sub[1]):
                    print("\033[1;31;40m ERR: Wront event type; Expected{0} got: {1} \033[0m".format(event.__class__,sub[1].__class__))
                    EventManager.errors.append("ERR: {0} event is insane. Data: {1} \033[0m".format(event.event,event.event_data))
                sub[0](event.event_data)   
            success = True   
        else:
            print("\033[1;33;40m WARN: {0} event has never had subscriptions \033[0m".format(event.event))
        return success
    
    #NOTE: atm there is no check if something makes multiple identical subscriptions.
    #IMO less code is better, and IMO EventManager should not be responsible for this
    def subscribe(event,callback,event_type):
        if not event in EventManager.subscriptions:
            EventManager.subscriptions[event] = []
        EventManager.subscriptions[event].append((callback,event_type))    #TODO: Ugly ugly touples, get rid of them
