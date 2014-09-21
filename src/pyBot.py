import main
class pyBot:
	def __init__(self):
		main.server = "irc.subluminal.net"
		main.port = 6667
		main.nick = "pyBot"
		main.login = "pyBot"
		main.realname = "pyBot"
		main.mode = "0"
		main.channel = "#" + input("Channel: #")
		main.connect()
