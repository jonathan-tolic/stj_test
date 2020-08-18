from flask import Flask
from events import *
from irc import *
from event_manager import *
app = Flask(__name__)

#What tangled Webs we wove
@app.route("/", endpoint='hello')
def hello():
    f= open('Main.html')
    html = f.read()
    f.close()
    return html

@app.route("/update/")
def update():
    global ws
    res = ""
    for m in ws.msgs:
        if len(res) >0: 
            res+=","
        res+='"{0}":"{1}"'.format(m.uu_type,m.uu_text)
    return "[{0}]".format(res)

@app.route("/request/")
def request():
    EventManager.triggerEvent(TextEventType("REQUEST","BY_THE_POWER_OF_GRAYSKULL"))
    return "request!"

#NOTE: would prefer using class based routes e.g. flask-classy, but this will do for now. Methods would beling to the WebServer
#Naturelly the WebServer would have its own file then
class WebServer:
    def __init__(self):
        self.msgs=[]
        
    def addMessage(self,msg):
        print("msg{0}".format(msg))
        self.msgs.append(msg)

#NOTE: this event solution is ambivalent as to using procedures or class methods. Thought I'd show an example. If moved to own class sould be segregated into own file
def writeLog(log):
    #if not isinstance(event,TextEventType):
        #print("\033[1;31;40m ERR: TextEvent expected; instead got {0} . Data: {1} \033[0m".format(event.event,event.event_data))
    try:
        f = open("log.txt",'a')
        f.write(log)
        f.write("\n")
        f.close()
    except: #TODO: add more precise exception handling reulsting in better user feedback; 
        EventManager.triggerEvent(UserUpdateEventType("ERROR","FAILED TO WRITE INTO LOG FILE"))

if __name__ == "__main__":
    global ws
    ws = WebServer()
    irc = IRC()
    #irc.start()
    EventManager.subscribe("USER_MESSAGE", ws.addMessage,UserUpdateEventType)
    EventManager.subscribe("WRITE_LOG",writeLog,TextEventType)
    EventManager.subscribe("WRITE_IRC",irc.sendEvent,TextEventType)
    EventManager.subscribe("REQUEST",writeLog,TextEventType)
    #EventManager.subscribe("REQUEST",irc.sendEvent,TextEventType)
    e = UserUpdateEventType("INFO","APP STARTED")
    EventManager.triggerEvent(e)
    print(EventManager.subscriptions)
    app.run()
    irc.stop()
