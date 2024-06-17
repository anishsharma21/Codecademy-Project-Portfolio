def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_list = [3, 5, 1, 7, 22, 3, 0]
print(bubble_sort(my_list))
# less than a minute