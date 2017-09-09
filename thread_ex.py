from threading import Thread, Lock, Semaphore, Condition
from time import sleep
count = 0
mutex = Lock()
sem = Semaphore()
cv = Condition()
cond = False

def print_count(count):
	sleep(.1)
	mutex.acquire()
	print(count)
	mutex.release()



def main():
	global count
	threads = [] 
	for i in range(100):
		thread = Thread(target = print_count, args = (count,))
		thread.start()
		mutex.acquire()
		threads.append(thread)
		count+=1
		mutex.release()

	for thread in threads:
		thread.join()

def second():
	sem.acquire()
	sem.release()

def third():
	cv.acquire()
	while not cond:
		cv.wait()
		print("done waiting")
	cv.release()
	print("done!")

def fourth():
	global cond
	cv.acquire() 
	cond = True
	cv.notifyAll()
	cv.release()
	print("released!")



if __name__ == "__main__":
	main()
	second()
	t1 = Thread(target = third)
	t2 = Thread(target =fourth)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
