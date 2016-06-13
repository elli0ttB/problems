from random import randint
from quicksort import quicksort
from merge import mergesort

def populate(n):
    return [randint(0,10) for i in range(n)]

def thirty_random_arrays():
    return [ populate(i) for i in range(30) ]

def _test_on_sort(sort):
    for case in thirty_random_arrays():
        expected = case[:]
        test = case[:]
        expected.sort()
        sort(case)
        assert expected == case

lomuto = lambda x : quicksort(x, "lomuto")
hoare = lambda x : quicksort(x, "hoare")

def test_lomuto():
    _test_on_sort(lomuto)

def test_hoare():
    _test_on_sort(hoare)

def test_mergesort():
    _test_on_sort(mergesort)


