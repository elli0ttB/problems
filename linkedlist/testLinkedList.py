import LinkedList as LL

# working on pg 90 of text, and reading solution to
# checking string uniqueness, I think I should be writing
# in C to ease thinking about complexity

def setup_function(fn):
    global linkedlist
    linkedlist = LL.Node(1)
    linkedlist.add(2)
    linkedlist.add(3)

def test_len():
    assert len(linkedlist) == 3

def test_remove_duplicates():
    linkedlist.add(3)
    linkedlist.add(3)
    linkedlist.add(1)
    linkedlist.add(2)
    removed = LL.remove_duplicates(linkedlist)
    assert len(removed) == 3

def test_remove_duplicates_stupidly():
    linkedlist.add(3)
    linkedlist.add(3)
    linkedlist.add(1)
    linkedlist.add(2)
    removed = LL.remove_duplicates_stupidly(linkedlist)
    assert len(removed) == 3

def test_nth_to_last():
    assert LL.nth_to_last(linkedlist, 0) == None
    assert LL.nth_to_last(linkedlist, 1) == 3
    assert LL.nth_to_last(linkedlist, 2) == 2
    assert LL.nth_to_last(linkedlist, 3) == 1
    assert LL.nth_to_last(linkedlist, 4) == None

def test_delete_node_in_middle():
    assert LL.delete_node_in_middle(linkedlist.next) == 2
    assert linkedlist.data == 1
    assert linkedlist.next.data == 3
    try :
        assert LL.delete_node_in_middle(linkedlist.next) == "should throw error"
    except ValueError:
        pass

def check_3_digits(result):
    assert result.data == 8
    assert result.next.data == 0
    assert result.next.next.data == 8


def setup_for_read_numbers():
    l1 = LL.Node(3)
    l1.add(1)
    l1.add(5)
    l2 = LL.Node(5)
    l2.add(9)
    l2.add(2)
    return l1, l2

def test_read_numbers():
    l1, l2 = setup_for_read_numbers()
    result = LL.add_decimal_numbers(l1, l2)
    check_3_digits(result)
    assert result.next.next.next == None

def test_read_numbers_with_different_sizes():
    l1, l2 = setup_for_read_numbers()
    l1.add(3)
    result = LL.add_decimal_numbers(l1, l2)
    check_3_digits(result)
    assert result.next.next.next.data == 3

def test_find_circle():
    head = LL.Node(5)
    n = head
    for i in range(10):
        n.next = LL.Node(i)
        n = n.next
    circle = head.next.next.next
    n.next = circle
    assert LL.find_circle(head) is circle
    circle.next = LL.Node(1)
    circle.next.next = circle
    assert LL.find_circle(head) is circle



