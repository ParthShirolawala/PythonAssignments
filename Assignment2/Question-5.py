#multiplying everything by 3 and output the result
import copy
numbers = [1,2,4,6,7,8]

def multiplyNumbers():
    number = copy.deepcopy(numbers)
    newnumber = []
    for i in number:
        newnumber.append(i*5)

    print newnumber
    print numbers

multiplyNumbers()