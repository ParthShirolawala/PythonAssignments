#write a program to print numbers whose cube is in range of 1 to 50.

def printNumber():
    number = []
    for i in range(5):
        if((i%2 != 0) and (i**3)<=50):
            number.append(i)
        else:
            continue

    print number


printNumber()