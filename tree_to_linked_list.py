def tree_to_ll(root):
	if root is None:
		return
	left = root.left
	right = root.right
	root.left = None
	tree_to_ll(left)
	tree_to_ll(right)
	root.right = left
	while root.right:
		root = root.right
	root.right= right