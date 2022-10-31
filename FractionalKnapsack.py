import numpy as np
def fractionak_Knapsack(w,v,c):
    l = list(zip(w,v))
    # using zip we have clubbed together weights and value as a 2d array
    x = []
    for i,j in l:
        ratio = j/i
        x.append(ratio)
        #ratios of value/weight is stored in this list 
    maximum_val = 0 
    #to get the max value with given capacity
    index = list(range(len(weights)))
    #we are creating list of index of number of elements in weights
    index.sort(key=lambda i:x[i],reverse=True)
    #here we map the x(val per unit weight)with the index
    for i in index:
        if(c>weights[i]):
            #if the capacity is greater than the weight at index i then add the value of weight at inex i and reduce the capacity equal to weight added
            maximum_val+=values[i]
            c-=weights[i]
        else:
            maximum_val+=c*x[i]
            # if the capacity is less than the weight at index i then add the product of the remaining capacity and ratio of value /weight at index i
            break
    print(maximum_val)
weights=[2,3,4,5]
values=[10,20,30,40]
c = 10
fractionak_Knapsack(weights,values,c)



