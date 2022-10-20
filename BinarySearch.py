#Binary Search
#this can be done using an recursive format or normal iterative format

#The detailed explanation is done in BinarySearch.pdf

def bin_search_recursion(arr,left,right,element):
    if right >= left:
        middle = (left + right) // 2

        if(arr[middle] == element):
            return middle
        elif(arr[middle] < element):
            #if the middle value is less than the element, we need to check
            #the right side of the array making the middle+1 index as the left index
            return bin_search_recursion(arr,middle+1,right,element)
        elif(arr[middle] > element):
            #if the middle value is greater than the element, we need to check
            #the left side of the array making the middle-1 index as the right index
            return bin_search_recursion(arr,left,middle-1,element)
    else:
        #when the searching element is not present in the array
        return -1

def bin_search_iteration(arr,left,right,element):
    while right+1 > left:
        middle = (left + right) // 2
        if(arr[middle] < element):
            #if the middle value is less than the element, we need to check
            #the right side of the array making the middle+1 index as the left index
            left = middle + 1
        elif(arr[middle] > element):
            #if the middle value is greater than the element, we need to check
            #the left side of the array making the middle-1 index as the right index
            right = middle
        elif(arr[middle] == element):
            return middle
    return -1

if __name__ == "__main__":
    arr = []

    while(True):
        temp = int(input("Enter Value : "))
        arr.append(temp)
        choice = input("Enter Y/y to continue or N/n to exit : ")
        if(choice == 'Y' or choice == 'y'):
            continue
        else:
            break
    
    print("\nEntered array : ",arr)
    print("For the Binary Search to work,the array needs to be sorted.")
    arr = sorted(arr) #sorting the array in ascending order
    print("Sorted Array : ",arr)

    element = int(input("Enter element to search in array : "))

    pos = bin_search_recursion(arr,0,len(arr)-1,element)
    if(pos == -1):
        print("Element not found in array.")
    else:
        print("Element found at index -> ",pos)

    pos = bin_search_recursion(arr,0,len(arr)-1,element)
    if(pos == -1):
        print("Element not found in array.")
    else:
        print("Element found at index -> ",pos)