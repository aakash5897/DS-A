class bs:
	def __init__(self,data=None):
		self.d=data
		self.sd=sorted(self.d)
		r=int(input("enter the element:"))
		self.high=len(self.d)-1
		self.sr(r,0)
	def sr(self,elem,low):
		if low>len(self.sd)-1:
			return ("not possible")
		else:
			mid=int(low+(self.high-low)/2)
			if self.sd[mid]==elem:
				print("match found at position %d"%(mid))
			elif self.sd.index(elem)>mid:
				low=mid+1
				return self.sr(elem,low)
			elif self.sd.index(elem)<mid:
				self.high=mid-1
				return self.sr(elem,low)
	
				
