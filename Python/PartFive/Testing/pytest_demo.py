from subtract import subtract

def test_subtract_netagive_numbers():
    result = subtract(-9, -11)
    assert result == 3
