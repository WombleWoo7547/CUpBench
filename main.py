import random
import time

def selection_sort(arr):
    if arr is None:
        return []
    # Traverse through all array elements
    for i in range(1, len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

print('Preparing...')
list = []
for i in range(1,1000000):
    list.append(i);
lnist = random.shuffle(list)

print('Starting...')

#print(list)

# Time the selection sort
start_time = time.time()
lenth = selection_sort(list)
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"Score is {duration / 100000}")