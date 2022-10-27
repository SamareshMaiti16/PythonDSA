class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
def fractionalknapsack(Capacity,arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)   
 
    # Result(value in Knapsack)
    finalvalue = 0.0
 
    # Looping through all Items
    for item in arr:
 
        # If adding Item won't overflow,
        # add it completely
        if item.weight <= Capacity:
            Capacity -= item.weight
            finalvalue += item.value
 
        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.value * Capacity/ item.weight
            break
     
    # Returning final value
    return finalvalue

Capacity = 50
arr = [Item(90, 10), Item(120, 20), Item(150, 30)]
    # Function call
max_val = fractionalknapsack(Capacity, arr)
print(max_val)
 