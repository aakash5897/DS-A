"""implementation of Linear Search"""
class ls:
	"""collecting data"""
	def __init__(self,data=None):
		self.d=data
	def sr(self,e=None):
		"""searching"""
		pos=0
		if not self.d:
			print("data not provided")
		else:
			for i in self.d:
				pos+=1
				if i==e:
					print("element found at position %d"%(pos))
					break
			else:
				print("not found")
	
				
