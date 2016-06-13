from is_rotation import is_rotation
def test_is_rotation():
    assert is_rotation("tool", "oolt")
    assert is_rotation("abcde", "cdeab")
    assert not is_rotation("the", "teh")
    assert not is_rotation("clown", "nwolc")
