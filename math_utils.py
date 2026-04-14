def modulo_sum(a, b, m):
    return (a + b) % m


if __name__ == "__main__":
    assert modulo_sum(17, 44, 15) == 1
    assert modulo_sum(-5, 12, 4) == 3
    assert modulo_sum(100, 200, 7) == 6
    print("All assertions passed.")
