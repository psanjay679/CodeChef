t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	a, b, s = [0] * n, [0] * n, [0] * n

	for i in range(n):
		a[i], b[i], s[i] = map(int, input().split())

	c, d, r = [0] * m, [0] * m, [0] * m

	for i in range(m):
		c[i], d[i], r[i] = map(int, input().split())

