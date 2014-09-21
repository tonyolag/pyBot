
class IrcManager:
    """
    IRC proprietary handlers 
    """
    def register(s, nick, login, mode, realname, channel):
        """
        Register on network
        """
        s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))
        s.send(("NICK " + nick + "\r\n").encode("utf-8"))
        s.send(("USER " + login + " " + mode + " * : " + realname + "\r\n").encode("utf-8"))
        s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))

        #inputThread should be added

        #A handler should exist here! [important]

class IrcParser:
    """
    Offers Parsing tools
    """
    def parse(line) :
        """
        Parse an irc line
        """
        result = list()
        splitter = line.split(" ")
        result.append(line.split("!")[0][1:].lower()) #Name
        result.append(splitter[0].split("!")[1].lower()) #Hostname
        result.append(splitter[1].lower()) #Action
        result.append(splitter[2].lower()) #Channel
        result.append(splitter[3][1:].lower()) #Command
        result.append(line.split(result[4]) + " "[1].lower()) #Arguments
        return result

