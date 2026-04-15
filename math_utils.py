def modulo_sum(a, b, m):
    return (a + b) % m


if __name__ == "__main__":
    assert modulo_sum(23, 19, 10) == 2
    assert modulo_sum(-7, 15, 5) == 3
    assert modulo_sum(81, 64, 11) == 2
    print("All assertions passed.")
