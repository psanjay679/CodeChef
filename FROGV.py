n, k, p = map(int, input().split())

ar = list(map(int, input().split()))

ar_pair = []

for index, value in enumerate(ar):
	ar_pair.append((value, index + 1))

ar_pair = sorted(ar_pair, key=lambda k: k[0])

# print (ar_pair)

_pair = ar_pair[0]
group = 0

dt = dict()
dt[_pair[1]] = group

for element in ar_pair:
	if (element[0] - _pair[0]) > k:
		group += 1

	dt[element[1]] = group
	_pair = element
# print (ar_pair)
# print (dt)

for _ in range(p):
	a, b = map(int, input().split())

	if dt[a] == dt[b]:
		print ('Yes')
	else:
		print ('No')