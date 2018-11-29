def quick_sort1(numlist):
    quick_sort2(list, 0, len(numlist)-1)

def quick_sort2(numlist,lo,hi):

    threshold = 1
    p = partition(numlist, lo, hi)
    quick_sort2(numlist, p-1, lo)
    quick_sort2(numlist, p+1, hi)

def partition(numlist, lo, hi):
    pass










    # pivot = len(list) - 1
    # left = 0
    # right = pivot - 1
    # if list(left) < pivot:
    #     left = left + 1