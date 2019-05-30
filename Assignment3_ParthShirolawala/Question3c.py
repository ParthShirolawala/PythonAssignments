#Implement Selection Sort

def selectionsort(input_list):

    for i in range(len(input_list)):
        smallest = i
        for j in range(i+1, len(input_list)):
            if(input_list[smallest] > input_list[j]):
                smallest = j

        temp = input_list[i]
        input_list[i] = input_list[smallest]
        input_list[smallest] = temp

    return input_list


input_list = [5,7,2,1,4,29,15]
input_list = selectionsort(input_list)
print(input_list)