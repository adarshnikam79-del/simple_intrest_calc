def simple_interest(p, r, t):
    return (p * r * t) / 100

def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100
    assert simple_interest(2000, 10, 1) == 200
    assert simple_interest(500, 4, 2) == 40
    print("All tests passed!")

if __name__ == "__main__":
    test_simple_interest()