#QuickSort Algorithm using two types of Partitioning technique

"""This is the swap function, where two values are swapped in the return statement"""
def swap_func(a,b):
    return b,a

"""This is the Hoare_Partition Technique. For further information consider the attached Quicksort.pdf file."""
def Hoare_Partition(arr,left_ptr,right_ptr):
    
    #The Pivot element is always chosen as the first element of the array
    pivot_element = arr[left_ptr]
    
    #The pointers are initially set outside the left and rightmost index.
    i = left_ptr - 1
    j= right_ptr + 1

    #Here the partition index is found out.
    while(True):
        i = i + 1
        while(arr[i] < pivot_element):
            i = i + 1
        
        j = j - 1
        while(arr[j] > pivot_element):
            j = j - 1
        
        if(i >= j):
            return j
        
        arr[i],arr[j] = swap_func(arr[i],arr[j])


"""This is the Lomuto_Partition Technique. For further information consider the attached Quicksort.pdf file."""
def Lomuto_Partition(arr,left_index,right_index):

    #The Pivot element is always chosen as the last element of the array
    pivot_element = arr[right_index]

    #The pointers are initially set outside the leftmost index.
    left_ptr = left_index - 1

    #Here the partition index is found out.
    for right_ptr in range(left_index,right_index):
        if(arr[right_ptr] <= pivot_element):
            left_ptr = left_ptr + 1
            arr[left_ptr],arr[right_ptr] = swap_func(arr[left_ptr],arr[right_ptr])

    arr[left_ptr+1],arr[right_index] = swap_func(arr[left_ptr+1],arr[right_index])
    return(left_ptr+1)


#The main driver function for the QuickSort_Hoare Algorithm
def QuickSort_Hoare(arr,left_ptr,right_ptr):
    if(left_ptr < right_ptr):
        partition_pivot = Hoare_Partition(arr,left_ptr,right_ptr)
        print("Pivot = ",partition_pivot )
        QuickSort_Hoare(arr,left_ptr,partition_pivot)
        QuickSort_Hoare(arr,partition_pivot+1,right_ptr)

#The main driver function for the QuickSort_Lomuto Algorithm
def QuickSort_Lomuto(arr,left_ptr,right_ptr):
    if(left_ptr < right_ptr):
        partition_pivot = Lomuto_Partition(arr,left_ptr,right_ptr)
        print("Pivot = ",partition_pivot )
        QuickSort_Lomuto(arr,left_ptr,partition_pivot-1)
        QuickSort_Lomuto(arr,partition_pivot+1,right_ptr)

#This is the main function
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

    choice = int(input("\n---------------QUICKSORT MENU SELECTION---------------\n\t1.Quicksort using Hoare Partition\n\t2.Quicksort using Lomuto Partition\nEnter your choice : "))
    if(choice == 1):
        length_array = len(arr)
        QuickSort_Hoare(arr,0,length_array-1)
        print("\nThe Sorted array is as follows : ")
        print(arr)
    elif(choice == 2):
        length_array = len(arr)
        QuickSort_Lomuto(arr,0,length_array-1)
        print("\nThe Sorted array is as follows : ")
        print(arr)
    else:
        print("\nInvalid Choice.")