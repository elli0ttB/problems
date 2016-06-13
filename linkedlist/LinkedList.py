class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def add(self, data):
        last = self
        while last.next != None:
            last = last.next
        last.next = Node(data)

    def __repr__(self):
        n = self
        list = []
        while n != None and str(n.data) not in list: # prevent infinite loops
            list.append(str(n.data))
            n = n.next
        return '{Node ' +  ', '.join(list) + '}'

    def __len__(self):
        n = self
        i = 0
        while n != None:
            i += 1
            n = n.next
        return i

def delete(head, d):
    """
    beautiful
    """
    n = head
    if n.data == d:
        return n.next
    while n.next != None:
        if n.next.data == d:
            n.next = n.next.next
            return head
        n = n.next

def remove_duplicates(head):
    n = head
    seen = set()
    seen.add(n.data)
    while n.next != None:
        d = n.next.data
        if d in seen:
            n.next = n.next.next
        else:
            n = n.next
            seen.add(d)
    return head

def contains(head, d):
    n = head
    while n != None:
        if n.data == d:
            return True
        n = n.next
    return False

def remove_duplicates_stupidly(head):
    n = head
    while n.next != None:
        if contains(n.next.next, n.next.data):
            n.next = n.next.next
        else:
            n = n.next
    if contains(head.next, head.data):
        return head.next
    else:
        return head

# __len__
# i =0
# n = head
# while n is not None:
#   i += 1
#   n = n.next
# return i

def get(head, i):
    if i < 0:
        return None
    n = head
    for _ in range(i):
        n = n.next
        if n == None:
            return None
    return n.data

def nth_to_last(head, i):
    if i < 1:
        return None
    i *= -1
    n = head
    while n != None:
        n = n.next
        i += 1
    if i < 0:
        return None
    n = head
    for _ in range(i):
        n = n.next
    return n.data

def their_nth_to_last(head, i):
    """ididnttestit"""
    if i < 1:
        return None
    p1 = p2 = head
    for _ in range(i-1):
        if p2 == None:
            return None
        p2 = p2.next
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    return p1.data

def delete_node_in_middle(middle):
    """
    delete the node in the middle of a linked list
    """
    result = middle.data
    if middle.next == None:
        raise ValueError("cant delete final node without head")
    middle.data = middle.next.data
    middle.next = middle.next.next
    return result

def copy(n):
    stub = Node(0)
    cp = stub

    while n != None:
        cp = cp.next = Node(n.data)
        n = n.next

    return stub.next

def data(n):
    if n == None:
        return 0
    else:
        return n.data

def next(n):
    if n == None:
        return None
    else:
        return n.next

def print_me(n):
    if n != None:
        print (n.data)
        print_me(n.next)
    else:
        print (None)

def add_decimal_numbers(l1, l2):
    """
    find the sum of two linked lists which encode numbers through reverse deciminal
    representation (i.e. head is 1s digit, tail is largest digit)
    """
    stub = Node(0)
    n = stub
    carry_over = 0
    while l1 != None or l2 != None:
        sum = data(l1) + data(l2)  + carry_over
        carry_over, digit = divmod(sum, 10)
        n.next = Node(digit)
        n = n.next
        l1 = next(l1)
        l2 = next(l2)
    return stub.next

def find_circle(head):
    """
    find the head of a linked list that has a loop down the pipeline
    """
    # be a do-while loop
    tortoise = head.next
    hair = head.next.next

    while tortoise is not hair:
        tortoise = tortoise.next
        hair = hair.next.next
    tortoise = head
    while tortoise is not hair:
        tortoise = tortoise.next
        hair = hair.next
    return tortoise




