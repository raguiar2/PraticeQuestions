import threading, time

sem1 = threading.Semaphore(0)
sem2 = threading.Semaphore(0)


def first():
	print("First")
def second():
	print("Second")
def third():
	print("Third")

def printfn(sem,thunk,nextsem):
	if not sem is None:
		sem.acquire()
	thunk()
	if not nextsem is None:
		nextsem.release()

if __name__=="__main__":
	t1 = threading.Thread(target=printfn,args=(None,first,sem1))
	t1.start()
	t2 = threading.Thread(target=printfn,args=(sem1,second,sem2))
	t2.start()
	t3 = threading.Thread(target=printfn,args=(sem2,third,None))
	t3.start()
	for thread in [t1,t2,t3]:
		thread.join()




