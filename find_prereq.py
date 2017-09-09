
def can_fufill_prereq(course, prereqs, completed):
	for prereq in prereq:
		if prereq[0] in completed:
			return True
	return False

def find_complete(required, prereq, completed):
	if required == []:
		return completed
	for course in required:
		if can_fufill_prereq(course, prereq, completed):
			tempreq = required
			tempreq.remove(course)
			completed.add(course)
			return find_complete(tempreq,prereq,completed)
	return []	



required = ['a','b','c','d','e','f']
prereq = [('a','b')]
print(find_complete(required, prereq, []))
