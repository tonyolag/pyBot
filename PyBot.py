import Main

class PyBot:
    """
    External Bot class
    """
    def __init__(self):
        """
        Initialize variables and Establish a connection
        """
        Main.server = "irc.subluminal.net"
        Main.port = 6667
        Main.nick = "pyBot"
        Main.login = "pyBot"
        Main.realname = "pyBot"
        Main.mode = "0"
        Main.channel = "#" + input("Channel: #")
        Main.connect()
