from colatz import next_collatz_element

def test_collatz_1():
    assert next_collatz_element(1) == 1
def test_collatz_2():
    assert next_collatz_element(2) == [2, 1]
def test_collatz_3():
     assert next_collatz_element(3) == [3, 10, 5, 16, 8, 4, 2, 1]
def test_collatz_4():
    assert next_collatz_element(4) == [4, 2, 1]
