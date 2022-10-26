def countingSort(arr):  #the func takes two inputs 1. Input array, 2. Maximum possible value in the array given by the user
    maxVal = max(arr) + 1 #finds the biggest number in the array
    output = [0] * len(arr) #create a output array where the final result will be calculated. Initially all the entries are 0
    valCount = [0] * maxVal #create a counting array where the count of each value in the input array is stored. Initially all the entries are 0
    #store the count of each element in the input array at their respective indexes in the count array
    for i in range(len(arr)):
        valCount[arr[i]] += 1
    #store the cumulative sum of the elements in the count array. This later helps to correctly place the sorted array
    for i in range(1,maxVal):
        valCount[i] += valCount[i - 1]
    i = len(arr) - 1
    #build the output array
    while i >= 0:
        #Find the index of each element in input array in the count array and store the element in that index of the output array
        output[valCount[arr[i]] - 1] = arr[i]
        #decrease the count of that element by 1
        valCount[arr[i]] -= 1
        #continue this process until the first element in the input array
        i -= 1
    #copy the contents of the output array to the input array so that it reflects the sorted array
    for i in range(len(arr)):
        arr[i] = output[i]


if __name__ == "__main__":
    print ("\n!!!Counting Sort does not work on negative or fractional numbers!!!\n!!!Do not input negative or fractional values in the array!!!\n")
    arr = [int(x) for x in input("\nEnter values into the array: ").split()]    #Take user input
    countingSort(arr=arr)   #sort the array
    print(f"Sorted array (ascending order): {arr}\n")   #Print the results