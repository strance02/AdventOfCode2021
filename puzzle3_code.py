with open('day2_input.txt') as f:
		data_prelim=f.readlines()

horizontal=0
depth=0

for entry in data_prelim:
	direction, mag = entry.split()
	if direction == "forward":
		horizontal+=int(mag)
	elif direction == "down":
		depth+=int(mag)
	elif direction == "up":
		depth-=int(mag)
	else:
		continue

print ("Horizontal position: ", horizontal)
print ("Depth: ", depth)
print (horizontal*depth)
