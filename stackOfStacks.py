CAPACITY=20

class SetOfStacks():

    def __init__(self):
        self.stacks = [Stack()]

    def push(self, d):
        stack = self.stacks[-1]
        stack.push(d)
        if len(stack) == CAPACITY:
            self.append(Stack())

    def pop(self):
        stack = self.stacks[-1]
        ans = stack.pop(d)
        if len(stack) == 0:
            self.stacks.pop()
        return ans

    def popAt(self, index):
        stack = self.stacks[index]
        ans = stack.pop()
        if len(stack) == 0:
            del self.stacks[index]
        return ans


class Node():
    def __init__(self, d, next=None):
        self.next = next
        self.data = d

class Stack():
    """
    stack implemented as linked list, with length
    """

    def __init__(self):
        self.top = None
        self.size = 0

    def _checkTop(self):
        if self.size == 0:
            raise ValueError("Empty Stack Error")

    def isEmpty(self):
        return size == 0

    def push(self, d):
        self.top = Node(d, next=self.top)
        self.size += 1

    def peek(self):
        _checkTop(self)
        return self.top.data

    def pop(self):
    def sort(self):
        """
        """

        _checkTop(self)
        self.size -= 1
        val = self.top.data
        self.top = self.top.next
        return val

    def __len__(self):
        return self.size

    def easy_sort(stack):
        ordered = Stack()
        while ! stack.isEmpty():
            tmp = stack.pop()
            while not ordered.isEmpty() and ordered.peek() < tmp:
                stack.push(ordered.pop())
            ordered.push(tmp)
        return ordered

    def sort(stack, ascending=True):
        if stack.isEmpty():
            return
        pivot = stack.peek()
        lessThan, greaterThan, equalTo = Stack(), Stack(), Stack()

        while not stack.isEmpty():
            top = stack.pop()
            if top < pivot:
                lessThan.push(top)
            elif top == pivot:
                equalTo.push(top)
            else:
                greaterThan.push(top)

        lessThan = sort(lessThan, ascending=True)
        greaterThan = sort(greaterThan, ascending=False)

        if ascending:
            ordered = lessThan
            backwards = greaterThan
        else:
            ordered = greaterThan
            backwards = lessThan

        while not equalTo.isEmpty():
            # TODO figure out stability
            ordered.push(equalTo.pop())
        while not backwards.isEmpty():
            ordered.push(backwards.pop())
        return orderd

class MyQueue():
    """
    queue implemented as two stacks
    this is not O(1), because sometimes we have to flip the stack.
    To be precise, we flip the stack whenever we dequeue all elements enqueued
    When we dequeue all elements enequeued before the last dequeue
    Bottom is flipped when  top is empty.
    Top is all elements that had been enqueued at the time of the last dequeue.

    Okay, it is O(1) since each element is enqueued and dequeued exactly once.
    """

    def __init__(self):
        self.top = Stack()
        self.bottom = Stack()

    def enqueue(self, val):
        bottom.push(val)

    def dequeue(self):
        if top.isEmpty():
            while not bottom.isEmpty():
                top.push(bottom.pop())
            if top.isEmpty():
                return None # return None when empty
        return top.pop()

    def __len__(self):
        return len(top) + len(bottom)

