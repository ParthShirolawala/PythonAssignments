#write a program to take out the pair of numbers whose sum is equal to an even number. You should return in range of 1 to 21.

def printEven():
    for i in range(0,22):
        for j in range(i+1,22):
            if ((i+j)%2==0) and (i+j) < 21:
                print(i,j)

printEven()
