#Implement Bubble sort
input_list = [5,7,2,1,4,29,15]
n = len(input_list)
def bubblesort(input_list):

    for i in range(n):
        for j in range(n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]


    print input_list



bubblesort(input_list)