with open('day3_input.txt') as f:
		data=data_fix=f.readlines()

#CALULATE OXYGEN
length=len(data[0])
for x in range(length-1): #why is it necessary to subtract 1??
	zero_count = one_count = 0
	data_zero=[]
	data_one=[]
	for number in data:
		if number[x]=='0':
			zero_count+=1
			data_zero.append(number) #making a list with the zero bit numbers
		else:
			one_count+=1
			data_one.append(number) #making a list with the one bit numbers
	if zero_count > one_count:
		data=data_zero
	else:
		data=data_one
	if(len(data)==1):
		break

oxygen=data[0]

print(int(oxygen,2))

#CALCULATE CO2
data=data_fix
for x in range(length-1):
	zero_count = one_count = 0
	data_zero=[]
	data_one=[]
	for number in data:
		if number[x]=='0':
			zero_count+=1
			data_zero.append(number)
		else:
			one_count+=1
			data_one.append(number)
	if zero_count > one_count:
		data=data_one
	else:
		data=data_zero
	if(len(data)==1):
		break

carbon=data[0]
print(int(carbon,2))

print(int(oxygen,2)*int(carbon,2))