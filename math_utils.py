def modulo_sum(a, b, m):
    return (a + b) % m


if __name__ == "__main__":
    assert modulo_sum(7, 8, 5) == 0
    assert modulo_sum(14, 11, 9) == 7
    assert modulo_sum(-3, 10, 4) == 3
    print("All assertions passed.")
