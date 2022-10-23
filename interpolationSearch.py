
#global variable to keep track of the number of iterations required to find the key
iterationCount = 0

####Sort Function to sort the input data

def heapsort(list):
    build_max_heap(list)  # Calling the max heap function to heapify the list
    for i in range(len(list) - 1, 0, -1):
        list[0], list[i] = list[i], list[0] #swwapping the first and last element of the list
        max_heapify(list, index=0, size=i)  #and again calling heapify on the root of the list
 
def parent(i):
    return (i - 1)//2   # the parent of a element(i) in a list is always located at index (i - 1) // 2 
 
def left(i):
    return 2*i + 1  #The left child of an element is always located at 2 * i  + 1
 
def right(i):
    return 2*i + 2  #The right child of an element is always located at 2 * i  + 2
 
def build_max_heap(list):
    length = len(list)
    start = parent(length - 1) 
    while start >= 0:
        max_heapify(list, index=start, size=length) #max_heapify is called on each parent node starting from the last parent node and working towards the root.
        start = start - 1
 
def max_heapify(list, index, size):
    l = left(index) #left child of index
    r = right(index)    #Right child of index
    if (l < size and list[l] > list[index]):
        largest = l #define left child as largest if it is greater than it's parent
    else:
        largest = index
    if (r < size and list[r] > list[largest]):
        largest = r #define right child as largest if it is greater than it's parent
    if (largest != index):
        list[largest], list[index] = list[index], list[largest] # swap the index element with it's right or left child if any of them is larger than the index
        max_heapify(list, largest, size)    #call max heapify on the new largest index to modify the lower branches to maintain the heap property

def interPolationSearch(arr, lo, hi, key):
    global iterationCount
    iterationCount += 1  #update iterationCount everytime the function is called
    if (lo <= hi and key >= arr[lo] and key <= arr[hi]):    #if the lower bound of the array is lower than the upper bound & the key can be present in the array
        if lo == hi:    #if the lower and upper bound of the list is same ie the length of the portion of that array is 1
            if key == arr[lo]:  #if the key is present in that array segment
                return lo   #return the position
            return -1   #if the key is not present in that portion it implies that it is not present in the array hence return -1
        #calculate the optimal position to search for the key based on the 
        #rate of increase of the data in the input array and the difference of the key from the smallest value in the array
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo])) * (key - arr[lo])
        if arr[pos] == key:
            return pos  #return the pos if the key is found
        elif key > arr[pos]: #if the key is larger than the element present at arr[pos]
            return interPolationSearch(arr, pos + 1, hi, key)   #run interpolation search on the upper portion of the array
        elif key < arr[pos]:    #if the key is smaller than the element present at arr[pos]
            return interPolationSearch(arr, lo, pos - 1, key)   #run interpolation search on the lower portion of the array
    #return -1 if the key is not found
    return -1

if __name__ == "__main__":
    arr = [int(x) for x in input("\nEnter values into the array: ").split()]    #take input for the input array
    key = int(input("\nEnter value to be searched: "))  #take input for the search key
    print (f"\nInput array: {arr}\n")
    heapsort(arr) #heap sort to sort the input data in ascending order
    print (f"\nSorted input array: {arr}\n")
    pos = interPolationSearch(arr=arr, lo=0, hi=len(arr) - 1, key=key)
    if pos == -1:   #if the key is not found in the supplied list we print that no such entry is detected
        print(f"\nThe value ({key}) is not found in the list.\n")
    else:   #if the key is found we print out its position in the list (starting at 0) and the iterations required to find it
        print(f"\nThe value ({key}) is found at position: {pos + 1} in the sorted inputlist.\niterations required: {iterationCount}\n")