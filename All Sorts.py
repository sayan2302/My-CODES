# SORTS in my code - Bubble sort , Insertion sort , Selection sort , Quick sort , Merge sort , Count sort


def bubble_sort(l):
    n=len(l)   
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def insertion_sort(l):
    for i in range(1,len(l)):
        while l[i-1]>l[i] and i>0:
            l[i],l[i-1]=l[i-1],l[i]
            i-=1
    return l

def selection_sort(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        if min!=i:l[i],l[min]=l[min],l[i]
    return l

def quick_sort(l):
    if len(l)<=1:
        return l
    pivot=l.pop()
    lower,greater=[],[]
    for i in l:
        if i>pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quick_sort(lower)+[pivot]+quick_sort(greater)

def count_sort(l):
    m=max(l)
    count=[0]*(m+1)
    for i in l:
        count[i]+=1
    for i in range(1,m+1):
        count[i]+=count[i-1]
    res=[0]*len(l)
    for i in l:
        j=count[i]-1
        res[j]=i
        count[i]-=1
    return res

def merge_sort(l):
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    L = l[:mid]
    R = l[mid:]

    merge_sort(L)
    merge_sort(R)

    # For joining two sorted arrays L and R
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        l[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        l[k] = R[j]
        j += 1
        k += 1
    return l

if __name__=="__main__":

    list=[0,5,12,1,2,6,0,34,34,3,4,2]
    print(merge_sort(list))
    print(count_sort(list))
    print(bubble_sort(list))
    print(insertion_sort(list))
    print(selection_sort(list))
    print(quick_sort(list))
