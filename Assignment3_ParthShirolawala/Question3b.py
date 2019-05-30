#Implement Quick sort
def quicksort(input_list):
    if len(input_list) == 1 or len(input_list) == 0:
        return input_list
    else:
        pivot = input_list[0]
        i = 0
        for j in range(len(input_list)-1):
            if input_list[j+1] < pivot:
                input_list[j+1], input_list[i+1] = input_list[i+1], input_list[j+1]
                i+=1
        input_list[0], input_list[i] = input_list[i], input_list[0]
        part1 = quicksort(input_list[:i])
        part2 = quicksort(input_list[i+1:])
        part1.append(input_list[i])
        return part1+part2




input_list = [5,7,2,1,4,29,15]
input_list = quicksort(input_list)
print(input_list)

