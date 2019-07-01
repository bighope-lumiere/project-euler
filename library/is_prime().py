"""
素数かどうかを判定する関数 is_prime() を定義
"""


def is_prime(n):
	if n == 1:
		return False

	for p in range(2, int(n ** 0.5) + 1):
		if n % p == 0:
			return False

	return True
