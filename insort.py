d=eval(input("enter the unsorted list:"))
for i in range(len(d)):
	if i+1==len(d):break
	else:
		if d[i+1]<d[i]:
			temp=d[i+1]
			d[i+1]=d[i]
			d[i]=temp
			j=i
			while(j):
				if d[j]<d[j-1]:
					temp=d[j]
					d[j]=d[j-1]
					d[j-1]=temp
					j-=1
				else:
					break
			
print("sorted list:",d)
