def modulo_sum(a, b, m):
    return (a + b) % m


assert modulo_sum(2, 3, 4) == 1
assert modulo_sum(10, 15, 7) == 4
assert modulo_sum(-1, 1, 5) == 0
