with open('day1_input.txt') as f:
	data=[int(line) for line in f.readlines()]


count=0
i=0
for num in data[1:]:
	if num > data[i]:
		count+=1
	i+=1

print(count)

# count=0
# for pos, num in enumerate(data[:-1]):
# 	if num < data[pos+1]:
# 		count+=1
		
# print(count)