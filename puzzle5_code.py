with open('day3_input.txt') as f:
		data=f.readlines()

gamma = epsilon = ''
length=len(data[0])
for x in range(length-1):
	zero_count = one_count = 0
	for number in data:
		if number[x]=='0':
			zero_count+=1
		else:
			one_count+=1
	if zero_count > one_count:
		gamma+='0'
		epsilon+='1'
	else:
		gamma+='1'
		epsilon+='0'

print(int(gamma,2), int(epsilon,2), int(gamma,2) * int(epsilon,2))
