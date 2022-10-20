#Assigining Count variable to 0, to keep track of the number of swap
count = 0

#The Merge Functions, which joins back the broken down array into a single sorted array
def merge_two(arr,left,middle,right):
    global count
    size1 = middle - left + 1
    size2 = right - middle

    left_array, right_array = [],[]

    for i in range(size1):
        left_array.append(arr[left+i])
    for j in range(size2):
        right_array.append(arr[middle+1+j])
    
    i,j,k = 0,0,left

    while(i<size1 and j<size2):
        if(left_array[i] <= right_array[j]):
            arr[k] = left_array[i]
            i = i+1
            k = k+1
            count = count+1
        else:
            arr[k] = right_array[j]
            j = j+1
            k = k+1
            count = count+1

    while(i < size1):
        arr[k] = left_array[i]
        i = i+1
        k = k+1
        count = count+1
    
    while(j < size2):
        arr[k] = right_array[j]
        j = j+1
        k = k+1
        count = count+1

def mergeSort(arr,left,right):
    if(left < right):
        middle = (left + right - 1)//2
        mergeSort(arr,left,middle)
        mergeSort(arr,middle+1,right)
        merge_two(arr,left,middle,right)

if __name__ == "__main__":
    arr = []
    print("\nEnter integer values inside the array.")
    while(True):
        temp = int(input("\nEnter Value : "))
        arr.append(temp)

        choice = int(input("\nEnter 1 to continue, 0 to Exit.\nEnter Choice : "))
        if(choice == 1):
            continue
        else:
            break

    length_array = len(arr)
    mergeSort(arr,0,length_array-1)
    print("\nSorted Array : ",arr)
    print("\nNumber of swaps : ",count)  