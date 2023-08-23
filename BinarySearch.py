import time
import random

# we will find time difference btwn naive search and binary search
def naive_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
    
def binary_search(arr,target,left,right):
    if right<left:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr, target, mid+1, right)
    else:
        return binary_search(arr, target, left, mid-1)
    
if __name__=="__main__":
    l=10000
    sorted_list=set()
    while l>0:
        sorted_list.add(random.randint(-l*5, l*5))
        l-=1
    sorted_list=sorted(list(sorted_list))
    start=time.time()
    for elem in sorted_list:
        naive_search(sorted_list, elem)
    end=time.time()
    print("Time taken by naive search: ",(end-start)/1000,"seconds")
    
    start=time.time()
    for elem in sorted_list:
        binary_search(sorted_list, elem,0,l)
    end=time.time()
    print("Time taken by Binary search: ",(end-start)/1000,"seconds")