from strings_anagrams import are_anagrams

def test_funny_anagrams():
    assert are_anagrams("the eyes", "they see")
    assert are_anagrams("Allahu Akbar, Obama", "Aha bub, koala alarm")
    assert are_anagrams("Donald Trump", "Damp Old Runt")

def test_same_is_anagram():
    assert are_anagrams("foo", "Foo")
    assert are_anagrams(" ", "   ")

def test_wrong():
    assert not are_anagrams("mary", "cow")
    assert not are_anagrams("123", "12345")

def test_explosion():
    assert not are_anagrams(None, "")
    assert not are_anagrams(321, 123)


