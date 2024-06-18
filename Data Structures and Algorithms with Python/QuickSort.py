def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = len(arr) // 2
    pivot_val = arr[pivot_idx]
    arr.pop(pivot_idx)
    less_than = list(filter(lambda x: x <= pivot_val, arr))
    greater_than = list(filter(lambda x: x > pivot_val, arr))
    if len(less_than) > 1:
        less_than = quick_sort(less_than)
    if len(greater_than) > 1:
        greater_than = quick_sort(greater_than)
    return less_than + [pivot_val] + greater_than

def quick_sort_with_pointers(arr, start, end):
    if start >= end:
        return
    pivot_idx = (start + end) // 2
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    less_than_pointer = start
    for i in range(start, end):
        if arr[i] < pivot_element:
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
    quick_sort_with_pointers(arr, start, less_than_pointer - 1)
    quick_sort_with_pointers(arr, less_than_pointer + 1, end)

my_list = [4, 3, 7, 2, 1, 5, 22, 0, 0, 22, 2]
# print(quick_sort(my_list))
quick_sort_with_pointers(my_list, 0, len(my_list)-1)
print(my_list)
# nice