def is_prime(n):
    """素数判定
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    if n%2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return 0
    return 1
