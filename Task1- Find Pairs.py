

def findPairs(arr, target):
    result = {}                         #Defining a dictionary

    for i in arr:
        if result.has_key(i):
            print i, result[i]
        key = target - i                #As we have to find the sum a+b=target. Now by doing this there will never be a key matching
                                        #to the one whose sum is not 10.
        result[key] = i



arr = [1, 2, 4, 6, 10,0,3]
findPairs(arr, 10)