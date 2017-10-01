def decode_ways(message, cache = {}):
	if message in cache:
		return cache[message]
	if message == "":
		return 1
	if message[0] == '0':
		return 0
	ways = decode_ways(message[1:])
	if len(message) > 1 and (message[0] < '2' or message[0] == '2' and message[1] < '7'):
		ways += decode_ways(message[2:])
	cache[message] = ways
	return ways 
