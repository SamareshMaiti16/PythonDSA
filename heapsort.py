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
 
if __name__ == "__main__":
    list = input('Enter the list of numbers: ').split() #Take user input to get the array of numbers
    list = [int(x) for x in list]   #modify the list to change all elements to integer
    heapsort(list)  #sort the list
    print('Sorted list: ', end='')  #print the sorted list
    print(list)