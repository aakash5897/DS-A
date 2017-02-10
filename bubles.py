"algorithm for bubble sort which takes Ο(n2) time"
d=eval(input("enter the unsorted list:"))
for i in range(len(d)):
		for j in range(len(d)):
			if j==len(d)-1:break
			if d[j+1]<d[j]:
				temp=d[j+1]
				d[j+1]=d[j]
				d[j]=temp
print("the sorted list is:",d)
