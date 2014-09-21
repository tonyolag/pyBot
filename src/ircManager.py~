class ircManager:
	def register(s, nick, login, mode, realname, channel):
		s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))
		s.send(("NICK " + nick + "\r\n").encode("utf-8"))
		s.send(("USER " + login + " " + mode + " * : " + realname + "\r\n").encode("utf-8"))
		s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))

		#inputThread should be added



	#A handler should exist here! [important]
