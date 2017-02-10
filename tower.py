"algorithm for towers of hanoi"
def tower(size,from_t,to_t,spare_t):
	if size==1:
		print("move disk from ", from_t,"to",to_t)
	else:
		tower(size-1,from_t,spare_t,to_t)
		tower(1,from_t,to_t,spare_t)
		tower(size-1,spare_t,to_t,from_t)
