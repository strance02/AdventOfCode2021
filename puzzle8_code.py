with open('day4_input.txt') as f:
		data = [line.strip() for line in f.readlines()]

drawn_numbers=(data[0].split(","))
data.pop(0)


for pos,i in enumerate(data):
	if i=='':
		data.pop(pos)
	data[pos]=data[pos].split()

boards_num=int(len(data)/5)
board_countdown=boards_num*[False]
losing_board, winning_number, unmarked_total=0,0,0

#Going number by number
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
				board_countdown[x]=True
								
		for y in range(5):
			if all(data[tracker][y]=='x' for tracker in range(tracker, tracker+5)):
				print(tracker,y)
				board_countdown[x]=True
						
		#Checking how many boards are yet to win
		if(board_countdown.count(False)==1):
			losing_board=(board_countdown.index(False))+1
		if(board_countdown.count(False)==0):	
			break

		tracker+=5

	if(board_countdown.count(False)==0):
		winning_number=int(number)
		break

#Separating the unmarked numbers from the losing board
tracker=losing_board*5
for i in range(tracker-5,tracker):
	for j in range(5):
		if(data[i][j]=='x'):
			continue
		else:
			unmarked_total+=int(data[i][j])

final=unmarked_total*winning_number


print(final)
print(unmarked_total, winning_number)
print(losing_board)	