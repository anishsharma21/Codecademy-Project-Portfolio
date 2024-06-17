def merge_sort(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if len(left) != 1:
        left = merge_sort(left)
    if len(right) != 1:
        right = merge_sort(right)
    temp_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            temp_arr.append(right[0])
            right.pop(0)
        else:
            temp_arr.append(left[0])
            left.pop(0)
    return temp_arr + left + right

my_list = [4, 3, 7, 2, 1, 5, 22, 0, 0, 22, 2]
print(merge_sort(my_list))