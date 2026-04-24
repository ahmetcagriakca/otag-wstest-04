def modulo_sum(a, b, m):
    return (a + b) % m


if __name__ == "__main__":
    assert modulo_sum(5, 7, 3) == 0
    assert modulo_sum(8, 9, 5) == 2
    assert modulo_sum(1, 2, 10) == 3
    print("All assertions passed.")
