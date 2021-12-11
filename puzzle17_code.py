with open('day9_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	
#print(data)
count=0

#print("LENGTH",len(data[0]))

for row_num, row in enumerate(data):
	for pos,char in enumerate(row):
		flag=True
		if pos!=(len(row)-1):
			if int(char) >= int(row[pos+1]):
				flag=False
		if pos!=0:
			if int(char) >= int(row[pos-1]):
				flag=False

		if row_num!=(len(data)-1):
			if int(char) >= int((data[row_num+1])[pos]):
				flag=False
		if row_num!=0:
			if int(char) >= int((data[row_num-1])[pos]):
				flag=False
		if flag == True:
			print(row_num,pos,char)
			count+=int(char) + 1

print(count)




