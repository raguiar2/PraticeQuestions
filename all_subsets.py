def all_subsets(s):
	if not s:
		return [[]]
	subsets = []
	for elem in s:
		s.remove(elem)
		smaller_subsets = all_subsets(s)
		subsets += smaller_subsets
		for smaller_subset in smaller_subsets:
			new_subset = smaller_subset[::]
			new_subset.insert(0,elem)
			subsets.append(new_subset)
	return subsets

print(all_subsets([1,2]))


