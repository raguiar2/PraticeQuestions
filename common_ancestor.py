def find_node(node, val):
	if node is None:
		return False
	if node == val:
		return True
	return find_node(node.left) or find_node(node.right)


def lowest_common_ancestor(node, descendant1, descendant2, depth):
	if not find_node(descendant1) or not find_node(descendant2):
		return -1
	if find_node(descendant1) and find_node(descendant2):
		return max(lowest_common_ancestor(node.left, descendant1, descendant2, depth+1),
			lowest_common_ancestor(node.left, descendant1, descendant2, depth+1), depth)
		




