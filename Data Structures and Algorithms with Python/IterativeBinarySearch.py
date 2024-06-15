def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list)
    while low != high:
        mid = (high + low) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            high = mid
        else:
            low = mid + 1
    return 'no value found'

l = [1, 3, 6, 9, 12, 16]
target = 2
print(binary_search(l, target))