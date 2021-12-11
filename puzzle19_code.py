def check_corrupted(line):
	global score
	for pos,char in enumerate(line):
		if char==')':
			if line[pos-1]=='(':
				line=line[:pos-1]+line[pos+1:]
				check_corrupted(line)
				break
			else:
				#print("FOUND",char)
				score+=3
				#print(score)
				return
		elif char==']':
			if line[pos-1]=='[':
				line=line[:pos-1]+line[pos+1:]
				check_corrupted(line)
				break
			else:
				#print("FOUND",char)
				score+=57
				#print(score)
				return
		elif char=='}':
			if line[pos-1]=='{':
				line=line[:pos-1]+line[pos+1:]
				check_corrupted(line)
				break
			else:
				#print("FOUND",char)
				score+=1197
				#print(score)
				return
		elif char=='>':
			if line[pos-1]=='<':
				line=line[:pos-1]+line[pos+1:]
				check_corrupted(line)
				break
			else:
				#print("FOUND",char)
				score+=25137
				#print(score)
				return

with open('day10_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	
#print(data)

score=0
for x in data:
	check_corrupted(x)
	
print(score)




