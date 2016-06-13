
# sometime, I should come back to this and do this with
# indices for the little arrays instead of slices.

def half_of(x):
    return int(x/2)

def merge(L, R, A):
    """
    we use A because we want to avoid
    allocating extra memory and can
    instead merge back into the caller
    """
    i,j,k = 0,0,0
    while k < len(A):
        if i == len(L) or (j < len(R) and L[i] > R[j]):
            A[k] = ( R[j] )
            j += 1
        else:
            A[k] = ( L[i] )
            i += 1
        k += 1

def mergesort(A):
    if len(A) < 2:
        return A
    else:
        x = half_of(len(A))
        L = A[:x]
        R = A[x:]
        mergesort(L)
        mergesort(R)
        # This way involves a lot less object creation,
        # because we don't replace the memory we allocate for L and R
        merge(L, R, A)

# Although we copy the entire array we are passed at each level (this would seem to imply O(n log(n)) memory usage), we, being program
# use a depth-first, not a breadth-first traversal of the program tree. At recursion depth n (we start at 0), the amount of memory we have allocated
# (if we are going along R every time is)
# is A + A/2 + A/4 + ... = A(2 -1/(2^n))
# we we need almost 2*n = O(n) additional memory, yikes.

#def bottom_up_merge(A):
#    """ this is terrible and I broke it."""
#    if len(A) < 2:
#        return
#    L = [ [i] for i in A ]
#    length = len(L)
#    while length > 1:
#        half = half_of(length)
#        for j in range(half):
#            copy = L[2*j][:]
#            L[j] *= 2
#            merge(copy, L[2*j+1], L[j])
#        L[half] = L[length -1]
#        length = half_of(length+1)
#    A[:] = L[0]
