class PushError(Exception):pass
class PopError(PushError):pass
class Stack:
	def __init__(self):
		r=int(input("enter the size of the Stack:"))
		self.d=[]
		self.r=r
	def push(self,item):
		if len(self.d)==self.r:
			raise PushError("stack is full!!!")
		else:
			self.d.append(item)
	def pop(self):
		if len(self.d)==0:
			raise PopError("stack is empty")
		else:
			p=self.d[-1]
			self.d=self.d[:len(self.d)-1]
			return ("popped %d"%(p))
	def __repr__(self):return repr(self.d)
			
