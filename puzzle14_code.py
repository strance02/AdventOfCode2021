with open('day7_input.txt') as f:
	data = f.readlines()
	data = data[0].split(",")
	data = [int(number) for number in data]

low=min(data)
high=max(data)
fuel_min=high-low

for x in range(low,high):
	fuel_count=0
	for num in data:
		diff=abs(num-x)
		while diff>0:
			fuel_count+=diff
			diff-=1
	if x==0:
		fuel_min=fuel_count
		pos=x
	if(fuel_count<fuel_min):
		fuel_min=fuel_count
		pos=x

print("Fuel",fuel_min)
print("position",pos)





