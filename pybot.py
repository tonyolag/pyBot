import socket

from irc import parse
# I left parse in it's own file, only to show you how it's done.
# When you've understood, move it into this class too, like register

class PyBot:
    """
    Main Bot Class
    """
    def __init__(self):
        """
        Initialize the bot
        """
        self.server = "irc.subluminal.net"
        self.port = 6667
        self.nick = "pyBot"
        self.login = "pyBot"
        self.realname = "pyBot"
        self.mode = "0"
        self.channel = "#" + input("Channel: #")

    def connect(self):
        """
        Initiate Connection and respond to commands
        """
        name = ""
        hostname  = ""
        chan = ""
        action = ""
        command = ""
        args = ""

        s = socket.socket() # rename this to something better, and store it in self. preferably during __init__.
        try:
            s.connect((self.server, self.port))
        except ConnectionRefusedError:
            print("Destination Net Unreachable")

        self.register(s, self.nick, self.login, self.mode, self.realname, self.channel)

        while True:
            line = s.recv(1024).decode("utf-8")
            if line:
                #line should be parsed here
                #Below code should be moved to ircManager.py
                print(str(line))
                if "001" in line:
                    s.send(("MODE " + self.mode + " +B\r\n").encode("utf-8"))
                    s.send(("JOIN " + self.channel+ "\r\n").encode("utf-8"))
                if "PING" in line[:4]:
                    s.send(("PONG " + line[5:] + "\r\n").encode("utf-8"))

    def register(self, s, nick, login, mode, realname, channel): # Unused arguments!
        """
        Register on network
        """
	#You also have no reason to be using arguments for this now, since it's in the same class and can use self.
        s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))
        s.send(("NICK " + nick + "\r\n").encode("utf-8"))
        s.send(("USER " + login + " " + mode + " * : " + realname + "\r\n").encode("utf-8"))
        s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))

        #inputThread should be added

        #A handler should exist here! [important]
        #Create and instantize a Handler class, and do something like handler.handle(line) here.

if __name__ == "__main__":
    """
    Create the bot and run it
    """
    bot = PyBot()
    bot.connect()

