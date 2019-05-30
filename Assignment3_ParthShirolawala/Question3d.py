def mergeSort(input_list):



   if len(input_list)>1:
       mid = len(input_list)//2
       left = input_list[:mid]
       right = input_list[mid:]


       mergeSort(left)
       mergeSort(right)

       i=0
       j=0
       k=0

       while i < len(left) and j < len(right):
           if left[i] < right[j]:
               input_list[k]=left[i]
               i=i+1
           else:
               input_list[k]=right[j]
               j=j+1
           k=k+1

       while i < len(left):
           input_list[k]=left[i]
           i=i+1
           k=k+1

       while j < len(right):
           input_list[k]=right[j]
           j=j+1
           k=k+1

   return input_list

input_list = [54,26,93,17,77,31,44,55,20]
input_list = mergeSort(input_list)
print(input_list)