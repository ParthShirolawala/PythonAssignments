#Check if all items are number in list

list = [2,4,5,7,"Parth"]

def checkInt(list):

    print(all(isinstance(i,int) for i in list))


checkInt(list)