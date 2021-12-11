def flash(octopus):
	
	global count
	flag=True
	while flag==True:
		for index in range(len(octopus)):
			length=len(octopus[index])
			for pos in range(length):
				#ADJACENT FLASH EFFECTS
				if octopus[index][pos]>9:
					octopus[index][pos]=0
					count+=1
					if pos < (length-1):
						if octopus[index][pos+1]!=0: #on the right (F)
							octopus[index][pos+1]+=1
						if index > 0 and octopus[index-1][pos+1]!=0: #right-above (C)
							octopus[index-1][pos+1]+=1
						if index < (len(octopus))-1 and octopus[index+1][pos+1]!=0: #right-below (I)
							octopus[index+1][pos+1]+=1
					
					if pos > 0:
						if octopus[index][pos-1]!=0: #on the left (D)
							octopus[index][pos-1]+=1
						if index > 0 and octopus[index-1][pos-1]!=0: #left-above (A)
							octopus[index-1][pos-1]+=1
						if index < (len(octopus))-1 and octopus[index+1][pos-1]!=0: #left-below (G)
							octopus[index+1][pos-1]+=1
					
					if index > 0 and octopus[index-1][pos]!=0: #above (B)
						octopus[index-1][pos]+=1
					if index < (len(octopus))-1 and octopus[index+1][pos]!=0: #below (H)
						octopus[index+1][pos]+=1
					
		flag=False
		for index in range(len(octopus)):
				for pos in range(len(octopus[index])):
					if octopus[index][pos]>9:
						flag=True
						break

	return octopus

with open('day11_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	
for pos,line in enumerate(data):
	temp=[]
	for char in line:
		temp.append(int(char))
	data[pos]=temp

count=0
sync=False
x=0
while sync==False:
	for index in range(len(data)):
			for pos in range(len(data[index])):
				data[index][pos]+=1

	data=flash(data)

	sync=True
	for index in range(len(data)):
			for pos in range(len(data[index])):
				if(data[index][pos]!=0):
					sync=False
	x+=1
	if x==100:
		print(count)
print(x)