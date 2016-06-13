#!/usr/bin/env python

def quicksort(arr, partition):
    if (partition == "hoare"):
        quicksort_hoare(arr, 0, len(arr) -1)
    elif (partition == "lomuto"):
        quicksort_lomuto(arr, 0, len(arr) -1)
    else:
        raise ValueError()

def quicksort_hoare(arr, lo, hi):
    # lo and hi follow standard method of being inclusive on the bottom, exclusive on the top.
    """Run a quicksort_hoare given a partition scheme"""
    if lo < hi:
        p = hoare(arr, lo, hi)
        quicksort_hoare(arr, lo, p)
        quicksort_hoare(arr, p+1, hi)

def quicksort_lomuto(arr, lo, hi):
    # lo and hi follow standard method of being inclusive on the bottom, exclusive on the top.
    """Run a quicksort_lomuto given a partition scheme"""
    if lo < hi:
        p = lomuto(arr, lo, hi)
        quicksort_lomuto(arr, lo, p-1)
        quicksort_lomuto(arr, p+1, hi)

def lomuto(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i # we know that arr[i] = p

def hoare(arr, lo, hi):
    pivot = arr[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i, j = i+1, j-1
        while arr[j] > pivot:
            j -= 1
        while arr[i] < pivot:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j

def main():
    import sort_test
    sort_test.test(lom)
    sort_test.test(hor)

if __name__ == "__main__":
    main()
