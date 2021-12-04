with open('day1_input.txt') as f:
	data_prelim=[int(line) for line in f.readlines()]

i=0
data=[]
for num in data_prelim:
	if (i+2) < len(data_prelim):
		a=num+data_prelim[i+1]+data_prelim[i+2]
		data.append(a)
		i+=1

count=0
i=-1
for num in data:
	if i!=-1:
		if num > data[i]:
			count+=1
	i+=1

print(count)
