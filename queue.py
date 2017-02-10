class qError(Exception):pass
class dError(qError):pass
class Queue:
	def __init__(self):
		r=int(input("enter queue size:"))
		self.r=r
		self.d=[]
		self.fr=0
		self.ra=0
	def enqueue(self,element):
		if self.fr==(self.r):
			raise qError(" queue is Full!!!")
		else:	
			self.d=[element]+self.d
			self.fr+=1
	def dequeue(self):
		if self.fr==self.ra:
			raise dError("Empty !!!")
		else:
			self.d=self.d[:-1]
			self.fr-=1
	def __repr__(self):return repr(self.d)
			
			
