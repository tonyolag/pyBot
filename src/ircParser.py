class ircParser:
	def parse(line) :
		result = list()
		splitter = line.split(" ")
		result.append(line.split("!")[0][1:].lower()) #Name
		result.append(splitter[0].split("!")[1].lower()) #Hostname
		result.append(splitter[1].lower()) #Action
		result.append(splitter[2].lower()) #Channel
		result.append(splitter[3][1:].lower()) #Command
		result.append(line.split(result[4]) + " "[1].lower()) #Arguments
		return result
