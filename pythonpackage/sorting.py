def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    l1 = items.copy()
    for i in range(len(l1)):
        for j in range(len(l1)-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]

    return l1


def merge_sort(items):
    def merge(A, B):    
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B    
        if len(B) == 0:
            new_list = new_list + A

        return new_list        
            
    
    len_i = len(items)
    if len_i == 1:
        return items       
        
    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])       
    
    return merge(i1, i2)


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[-1]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
