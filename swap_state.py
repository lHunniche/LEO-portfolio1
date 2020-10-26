file = open("state.txt", "r")

def write_state(new_state):
	write_file = open("state.txt", "w")
	write_file.write(new_state)
	write_file.close()

if file.readline() == "1":
	file.close()
	write_state("0")
else:
	file.close()
	write_state("1")


