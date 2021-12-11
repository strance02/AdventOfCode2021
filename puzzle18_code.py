def find_neighbours(row_index,pos_index,height_map,height2,number):
	global counter
	row=height_map[row_index]
	if (height2[row_index])[pos_index] != '9':
		counter+=1
		#print("CONSIDERING:",row_index,pos_index,number)
		if pos_index!=(len(height_map[row_index])-1):
			if int(row[pos_index+1])!=9 and (int(row[pos_index+1])-int(number))>=1:
				#print("CONDITION 1:")
				find_neighbours(row_index,pos_index+1,height_map,height2,int(row[pos_index+1]))
						
		if pos_index!=0:
			if int(row[pos_index-1])!=9 and (int(row[pos_index-1])-int(number))>=1:
				#print("CONDITION 2:")
				find_neighbours(row_index,pos_index-1,height_map,height2,int(row[pos_index-1]))
			
		if row_index!=(len(height_map)-1):
			temp=int((height_map[row_index+1])[pos_index])
			if temp!=9 and temp-int(number)>=1:
				#print("CONDITION 3:")
				find_neighbours(row_index+1,pos_index,height_map,height2,temp)
				
		if row_index!=0:
			temp2=int((height_map[row_index-1])[pos_index])
			if temp2!=9 and temp2-int(number)>=1:
				#print("CONDITION 4:")
				find_neighbours(row_index-1,pos_index,height_map,height2,temp2)
	s=list(height2[row_index])
	s[pos_index]="9"
	height2[row_index]="".join(s)
	#print(height2)

with open('day9_input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	
#print(data)
count=0

#print("LENGTH",len(data[0]))
basins=[]
for row_num, row in enumerate(data):
	count=0
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
			#print(row_num,pos,char)
			counter=0
			find_neighbours(row_num,pos,data,data,int(char))
			#print("DONE",counter)
			if counter!=0:
				basins.append(counter)

basins.sort()
basins.reverse()
#print(basins)
final=1
for x in basins[:3]:
	final*=x
#print(len(basins))
print(final)










