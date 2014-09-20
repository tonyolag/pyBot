import socket
server = "irc.subluminal.net"
port = 6667
nick = "pyBot"
login = "pyBot"
realname = "pyBot"
mode = "0"
line = ""
channel = "#" + input("Channel: #")
s = socket.socket()
s.connect((server, port))
s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))
s.send("NICK ".encode("utf-8") + nick.encode("utf-8") + "\r\n".encode("utf-8"))
s.send("USER ".encode("utf-8") + login.encode("utf-8") + " ".encode("utf-8") + mode.encode("utf-8") + " * : ".encode("utf-8") + realname.encode("utf-8") + "\r\n".encode("utf-8"))
s.send("PONG ".encode("utf-8") + s.recv(1024)[5:] + "\r\n".encode("utf-8"))

while True:
	line = s.recv(1024).decode("utf-8")
	if line:
		print (str(line))
		if "001" in line:
			s.send("MODE ".encode("utf-8") + mode.encode("utf-8") + " +B\r\n".encode("utf-8"))
			s.send("JOIN ".encode("utf-8") + channel.encode("utf-8") + "\r\n".encode("utf-8"))
		if "PING" in line[:4]:
			s.send("PONG ".encode("utf-8") + line[5:].encode("utf-8") + "\r\n".encode("utf-8"))




