t = int(input())

for _ in range(t):
	n = int(input())
	ar = list()
	maxColinRow = list()
	for i in range(n):
		_ar = list(input())
		ar.append(_ar)
		_maxColinRow = -1
		for j, k in enumerate(_ar):
			if k == '#':
				_maxColinRow = j

		maxColinRow.append(_maxColinRow)

	count = 0
	for col in range(n-1, -1, -1):
		for row in range(n-1, -1, -1):
			if ar[row][col] == '#': # discard the column completely
				break
			elif maxColinRow[row] >= col:
				continue
			else:
				count += 1
	print (count)
