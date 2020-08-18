import socket
import sys
from threading import Thread
from time import sleep

class IRC(Thread):
    irc = socket.socket()
    def __init__(self):  
        Thread.__init__(self)
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG {0} {1}\n".format(chan, msg ).encode())

    def connect(self, server, channel, botnick):
        self.irc.connect((self.server, 6667))
        self.irc.send("USER {0} {0} {0} :The Machine is immortal!\n".format(botnick).encode())
        self.irc.send("NICK {0}\n".format(botnick).encode())               
        self.irc.send("JOIN {0}\n".format(self.channel).encode())

    def getText(self):
        text=self.irc.recv(2040).decode()

        if text.find('PING') != -1:                      
            self.irc.send('PONG {0}\n'.format(text.split() [1]).encode()) 

        return text

    def sendEvent(self, msg):
        self.send(self.channel,msg)

    def run(self):
        self.channel = "#stj_testing"
        self.server = "irc.freenode.net"
        self.nickname = "botty_the_bot"
        
        self.connect(self.server, self.channel, self.nickname)
        while 1:
            sleep(2)
            text = self.getText()
            if "PRIVMSG" in text and self.channel in text and "hello" in text:
                self.send(self.channel, "Praise_the_Omnissiah!")

