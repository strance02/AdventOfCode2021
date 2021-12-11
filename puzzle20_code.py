def check_corrupted(line,index):
	global score
	global flag
	for pos,char in enumerate(line):
		if char==')':
			if line[pos-1]=='(':
				line=line[:pos-1]+line[pos+1:]
				data[index]=line
				check_corrupted(line,index)
				break
			else:
				#print("FOUND",char)
				score+=3
				#print(score)
				flag=False
				return
		elif char==']':
			if line[pos-1]=='[':
				line=line[:pos-1]+line[pos+1:]
				data[index]=line
				check_corrupted(line,index)
				break
			else:
				#print("FOUND",char)
				score+=57
				#print(score)
				flag=False
				return
		elif char=='}':
			if line[pos-1]=='{':
				line=line[:pos-1]+line[pos+1:]
				data[index]=line
				check_corrupted(line,index)
				break
			else:
				#print("FOUND",char)
				score+=1197
				#print(score)
				flag=False
				return
		elif char=='>':
			if line[pos-1]=='<':
				line=line[:pos-1]+line[pos+1:]
				data[index]=line
				check_corrupted(line,index)
				break
			else:
				#print("FOUND",char)
				score+=25137
				#print(score)
				flag=False
				return

def complete(line):
	total=0
	for x in reversed(line):
		total*=5
		if x=='(':
			total+=1
		elif x=='[':
			total+=2
		elif x=='{':
			total+=3
		else:
			total+=4
	return total

with open('day10_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	
#print(data)

score=0
for pos,x in enumerate(data):
	flag=True
	check_corrupted(x,pos)
	if(flag==False):
		data[pos]=""

data=[x for x in data if x!='']

#print(data)	
print("PART 1:",score)

#calculating scores of completed sequences
scores=[]
for x in data:
	temp=complete(x)
	scores.append(temp)

scores.sort()

#finding middle score
print("PART 2:",scores[int((len(scores)/2)-0.5)])







