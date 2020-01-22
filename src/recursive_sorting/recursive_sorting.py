# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a_index = b_index = 0
    for i in range(0, elements):
        # a empty, b not empty
        if a_index >= (len(arrA)):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        # b empty, a not empty
        elif b_index >= (len(arrB)):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrB[b_index] <= arrA[a_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
### recursive sorting function
def merge_sort( arr ):
    # Recursively split the array into smaller lists down the middle until everything is in a single-item list
    if len(arr) > 1:
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
