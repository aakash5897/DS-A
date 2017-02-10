d=eval(input("enter an unsorted list"))
mid=int(len(d)/2)
l=d[:mid]
r=d[mid:]
for i in l:
	for j in l[i:]:
		if d[j]<d[i]:
			temp=d[j]
			d[j]=d[i]
			d[i]=temp
		else:continue
print(d)
