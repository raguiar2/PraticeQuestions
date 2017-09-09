import collections

def char_mapping(mapping,string,ans = ""):
	if not string:
		print(ans)
		return
	char = int(string[0])
	for ch in mapping[char]:
		char_mapping(mapping,string[1:],ans + ch)


mapping = collections.defaultdict(list)

mapping[1] = ['a','b','c']
mapping[2] = ['d','e']

char_mapping(mapping,'12')