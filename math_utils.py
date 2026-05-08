def modulo_sum(a, b, m):
    return (a + b) % m


if __name__ == "__main__":
    assert modulo_sum(2, 3, 4) == 1
    assert modulo_sum(10, 5, 7) == 1
    assert modulo_sum(9, 6, 4) == 3
    print("All assertions passed.")
