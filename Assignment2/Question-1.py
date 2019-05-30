#write a program to take out the element from their index values:

x = [1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_", 5+5j], 4000]

def printElement():
    print(x[4][:2])
    print(x[4][6])
    print(x[4][4][2:])
    print(x[4][3:6])


printElement()