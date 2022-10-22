
#global variable to keep track of the number of iterations required to find the key
iterationCount = 0

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
    print ("\n!!!Interpolation Search only works for sorted inputs!!!\n!!!Only enter sorted input!!!\n")
    arr = [int(x) for x in input("\nEnter values into the array: ").split()]    #take input for the input array
    key = int(input("\nEnter value to be searched: "))  #take input for the search key
    pos = interPolationSearch(arr=arr, lo=0, hi=len(arr) - 1, key=key)
    if pos == -1:   #if the key is not found in the supplied list we print that no such entry is detected
        print(f"\nThe value ({key}) is not found in the list.\n")
    else:   #if the key is found we print out its position in the list (starting at 0) and the iterations required to find it
        print(f"\nThe value ({key}) is found at position: {pos} in the list.\niterations required: {iterationCount}\n")