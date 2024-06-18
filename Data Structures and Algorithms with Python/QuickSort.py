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

my_list = [4, 3, 7, 2, 1, 5, 22, 0, 0, 22, 2]
print(quick_sort(my_list))
# nice