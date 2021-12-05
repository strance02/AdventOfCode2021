with open('day4_input.txt') as f:
		data = f.readlines()
		data = [line.strip() for line in data]

drawn_numbers=(data[0].split(","))
data.pop(0)


for pos,i in enumerate(data):
	if i=='':
		data.pop(pos)
	data[pos]=data[pos].split()

boards_num=int(len(data)/5)
winning_board=0
winning_number=0
unmarked_total=0

for number in drawn_numbers:
	tracker=0
	#Check the number against each board
	for row in data:
		for pos,col in enumerate(row):
			if col==number:
				row[pos]='x'
			else:
				continue
	
	for x in range(boards_num):
		for row in data[tracker:tracker+5]:
			if all(r=='x' for r in row):
				winning_board=x+1
				break
		for y in range(5):
			if all(data[tracker][y]=='x' for tracker in range(tracker, tracker+5)):
				winning_board=x+1
				break
		if(winning_board!=0):
			break
		tracker+=5
	if(winning_board!=0):
		winning_number=int(number)
		break

#Separating the unmarked numbers from the winning board
for i in range(tracker,tracker+5):
	for j in range(5):
		if(data[i][j]=='x'):
			continue
		else:
			unmarked_total+=int(data[i][j])

final=unmarked_total*winning_number

print(final)
print(unmarked_total, winning_number)
print(winning_board)




	