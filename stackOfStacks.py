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
        _checkTop(self)
        self.size -= 1
        val = self.top.data
        self.top = self.top.next
        return val

    def __len__(self):
        return self.size

    def sort(self):
        """
        First understand what the problem is!!!
        """

        """

        1 --- done
        2 --- a = pop()

        what sort works well with a stack
        bubble sort?
        a & b

        We need to sort the stack. Ideally, it should be in O(nlog(n)) time.
        Presumably, we should use O(1) extra memory.

        One way would be to copy it into an array, quicksort the array, and
        then push it back onto the stack. That is probably what I would typically do

        list = []
        while not self.isEmpty:
            list.append(self.pop())
        quicksort(list) # ascending
        for item in reversed(list):
            stack.push(item)

        can we partition the stack
        """

        def main_sort(stack):
            sort(stack, False)

        def sort(stack, reversed):
            if stack.isEmpty():
                return

            # do a quicksort partition, except using more memory
            pivot = stack.peek()
            lessThan = Stack()
            greaterThan = Stack()
            equalTo = Stack()
            while not stack.isEmpty():
                # We do this to avoid the problem that occors when the
                # input is all equal.
                a = stack.pop()
                if a < pivot:
                    lessThan.push(a)
                elif a == pivot:
                    equalTo.push(a)
                else:
                    greaterThan.push(a)

            # recursively sort the sub-stacks
            # we sort greaterThan oppossite the order
            # we are sorted for ease of concatenation.
            # an alternative would be to sort lessThan in opposite order,
            # clear the stack and push it back onto itself, but this is simpler.
            lessThan = sort(lessThan, reversed)
            greaterThan = sort(greaterThan, not reversed)

            # greaterThan is sorted in reverse order, so we can
            # concatanate it to lessThan
            if reversed:
                lessThan, greaterThan = greaterThan, lessThan

            # normally this does keep the sort stable, but what
            # happens when reversed is true?
            while not equalTo.isEmpty():
                lessThan.push(equalTo.pop())

            while not greaterThan.isEmpty():
                lessThan.push(greaterThan.pop())

            # we cannot copy memory efficiently, so let's just return the result'

        # I should look at how mergeSort uses working memory!!!


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

