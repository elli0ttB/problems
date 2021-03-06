#!/usr/bin/env python

# Top down mergesort is like the recursive implementation of quicksort that I
# learned, but it uses a scratch array for each stage of the merge and copies back the merged parts into A as they are constructued

# work flow is
    # get Parts of A that you are sorting in this frame
    # copy them into B
    # sort them in B
    # copy them back to A

    # we have to do it that way because we are in C and can't allocate array memeory willy-nilly'

    # If we were in python, we would just allocate the bits and pieces that we need as we go, # but in C we are going to have all our memory storage allocated up front
# Array A[] has the items to sort; array B[] is a work array.
TopDownMergeSort(A[], B[], n) {
    TopDownSplitMerge(A, 0, n, B);
}

# iBegin is inclusive; iEnd is exclusive (A[iEnd] is not in the set).
TopDownSplitMerge(A[], iBegin, iEnd, B[]) {
    if(iEnd - iBegin < 2)                       # if run size == 1
        return;                                 #   consider it sorted
    # recursively split runs into two halves until run size == 1,
    # then merge them and return back up the call chain
    iMiddle = (iEnd + iBegin) / 2;              # iMiddle = mid point
    TopDownSplitMerge(A, iBegin,  iMiddle, B);  # split / merge left  half
    TopDownSplitMerge(A, iMiddle,    iEnd, B);  # split / merge right half
    TopDownMerge(A, iBegin, iMiddle, iEnd, B);  # merge the two half runs
    CopyArray(B, iBegin, iEnd, A);              # copy the merged runs back to A
}

#  Left half is A[iBegin:iMiddle-1].
# Right half is A[iMiddle:iEnd-1   ].
TopDownMerge(A[], iBegin, iMiddle, iEnd, B[]) {
    i = iBegin, j = iMiddle;

    # While there are elements in the left or right runs...
    for (k = iBegin; k < iEnd; k++) {
        # If left run head exists and is <= existing right run head.
        if (i < iMiddle && (j >= iEnd || A[i] <= A[j])) {
            B[k] = A[i];
            i = i + 1;
        } else {
            B[k] = A[j];
            j = j + 1;
        }
    }
}

CopyArray(B[], iBegin, iEnd, A[]) {
    for(k = iBegin; k < iEnd; k++)
        A[k] = B[k];
}
