from threading import Lock, Thread, Semaphore

lock = Lock()
nextnum = Semaphore(1)
div_three_sem, div_five_sem, div_both_sem = Semaphore(0), Semaphore(0), Semaphore(0)
sems = [div_three_sem, div_five_sem, div_both_sem]
num = 0
brk = False

def divis_by_three():
	global nextnum
	global lock
	global div_three_sem
	global brk
	while not brk:
		div_three_sem.acquire()
		if brk: 
			nextnum.release()
			break
		lock.acquire()
		if num % 3 == 0 and num % 5 != 0:
			print("Fizz")
		lock.release()
		nextnum.release()


def divis_by_five():
	global nextnum
	global lock
	global div_five_sem
	global brk
	while not brk:
		div_five_sem.acquire()
		if brk: 
			nextnum.release()
			break
		lock.acquire()
		if num % 3 != 0 and num % 5 == 0:
			print("Buzz")
		lock.release()
		nextnum.release()


def divis_by_both():
	global nextnum
	global lock
	global div_both_sem
	global brk
	while not brk:
		div_both_sem.acquire()
		if brk: 
			nextnum.release()
			break
		lock.acquire()
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz")
		lock.release()
		nextnum.release()



def numbers():
	global nextnum
	global num
	global lock
	global sems
	global brk
	while num <= 100:
		lock.acquire()
		num += 1
		lock.release()
		for sem in sems:
			sem.release()
		for i in range(3):
			nextnum.acquire()
	brk = True
	for sem in sems:
			sem.release()
	for i in range(3):
		nextnum.acquire()


if __name__=="__main__":
	div_three_thread = Thread(target = divis_by_three)
	div_five_thread = Thread(target = divis_by_five)
	div_both_thread = Thread(target = divis_by_both)
	numbers_sem = Thread(target = numbers)
	threads = [div_three_thread,div_five_thread,div_both_thread,numbers_sem]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()


