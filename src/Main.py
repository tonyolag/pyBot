import socket
from ircManager import ircManager #Handler Should be imported
# ^ ImportError: cannot import name 'register'
class main:
"""
Main Bot Class
"""
    def connect(self) :
        """
        Initiate Connection and respond to commands
        """
        self.server = ""
        self.port = 6667
        self.nick = ""
        self.login = ""
        self.realname = ""
        self.mode = ""
        self.line = ""
        self.channel = ""
        
        self.name = ""
        self.hostname  = ""
        self.chan = ""
        self.action = ""
        self.command = ""
        self.args = ""

        s = socket.socket()
        try:
            s.connect((server, port))
        except ConnectionRefusedError:
            print("Destination Net Unreachable")


        register(s, nick, login, mode, realname, channel)

        while True:
            line = s.recv(1024).decode("utf-8")
                if line:
                    #line should be parsed here
                    #Below code should be moved to ircManager.py
                    print (str(line))
                    if "001" in line:
                        s.send(("MODE " + mode + " +B\r\n").encode("utf-8"))
                        s.send(("JOIN " + channel+ "\r\n").encode("utf-8"))
                    if "PING" in line[:4]:
                        s.send(("PONG " + line[5:] + "\r\n").encode("utf-8"))





