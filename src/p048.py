"""
数字が膨大にならないように INF = 10 ** 10 で割りながら計算するように注意する。
"""


def self_pow(n):
	res = 1
	for i in range(n):
		res *= n
		n %= INF
	return res


INF = 10 ** 10
ans = 0
for i in range(1, 1001):
	ans += self_pow(i)
	ans %= INF
print(ans)
