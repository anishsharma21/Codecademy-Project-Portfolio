def binary_search(sorted_list, target, low=None, high=None):
    if low == None:
        low = 0
        high = len(sorted_list)

    if low == high:
        return 'value not found'
    mid = (high + low) // 2
    if sorted_list[mid] == target:
        return mid
    
    if sorted_list[mid] > target:
        return binary_search(sorted_list, target, low, high=mid)
    else:
        result = binary_search(sorted_list, target, low=mid+1, high=high)
        return result
    

my_list = [0, 2, 5, 7, 12, 33, 39]
target = 5
index_of_target = binary_search(my_list, 45)
print(index_of_target)
