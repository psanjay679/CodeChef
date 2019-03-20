t = int(input())

for _ in range(t):
	n, k = map(int, input().split())
	ar = list(map(int, input().split()))
	maxXor = 0 ^ k

	for i in range(n):
		xor = ar[i]
		for j in range(i + 1, n):
			xor = ar[j]
			maxXor = max(maxXor, k ^ xor)
		maxXor = max(maxXor, k ^ xor)

	print (maxXor)
