with open('day5_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	data = [line.split(" -> ") for line in data]

grid=[]
for i in range(1000):
	row=[]
	for j in range(1000):
		row.append(0)
	grid.append(row)

#print(data)

for line in data:
	coord1=line[0].split(",")
	coord2=line[1].split(",")
	x1=int(coord1[0])
	y1=int(coord1[1])
	x2=int(coord2[0])
	y2=int(coord2[1])
	
	if y1==y2:
		if x1<x2:
			for x in range(x1,x2+1):
				grid[y1][x]+=1
				
		else:
			for x in range(x2,x1+1):
				grid[y1][x]+=1
	elif x1==x2:
		if(y1<y2):
			for y in range(y1,y2+1):
				grid[y][x1]+=1
		else:
			for y in range(y2,y1+1):
				grid[y][x1]+=1

	#print(grid)

count=0
for row in grid:
	for col in row:
		if col>1:
			count+=1

print(count)



