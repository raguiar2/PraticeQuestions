import Queue

def djikstra(point1, point2):
	pq = Queue.PriorityQueue()
	visited = []
	visited.put(point1,0)
	cost = 0
	while not pq.empty():
		point = pq.get()
		cost = a[1]
		for neghibor in get_neghibor(point):
			if neghibor == point2:
				cost += neghibor
				print(cost)
				return
			if neghibor not in visited:
				pq.put(neghibor, cost+neghibor)


