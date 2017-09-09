SUM = 100


def one_to_nine(numbers, ans):
	if not numbers:
		if eval(ans) == SUM:
			print(ans)
		return
	if ans:
		one_to_nine(numbers[1:], ans + '+' + numbers[0])
	one_to_nine(numbers[1:], ans + '-' + numbers[0])
	one_to_nine(numbers[1:], ans + numbers[0])

one_to_nine('123456789','')

