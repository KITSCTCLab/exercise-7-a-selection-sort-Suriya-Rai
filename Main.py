from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(len(size)):
    min = i
    for j in range(j=i+1,len(size)):
      if array[min] > array[j]:
          min = j
                             
    array[i],array[min] = array[min],array[i]
                             

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
