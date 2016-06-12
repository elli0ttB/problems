from stackOfStacks import Stack

def solve(n, S, M, G):
    if n == 0:
        return
    print "Level %d:" % n
    solve(n-1, S, G, M)
    G.push(S.pop())
    solve(n-1, M, S, G)

def hanoi_solve(S, M, G):
    """
    solve the towers of hanoi puzzle with the given stacks
    M and G should be empty.
    """
    solve(len(S), S, M, G)

class HanoiStack(Stack):
    """
    Like Stack, but can only push smaller values
    """

    def __init__(self):
        Stack.__init__(self)

    def push(self, d):
        if self.top and d >= self.top.data:
            raise ValueError("tried to push %d when top was %d" % (d, self.top.data))
        Stack.push(self, d)

S = HanoiStack()
M = HanoiStack()
G = HanoiStack()

for i in reversed(range(1,5)):
    S.push(i)

hanoi_solve(S,M,G)
