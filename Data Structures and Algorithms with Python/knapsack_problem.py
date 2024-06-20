count = 0
def recursive_knapsack(weight_cap, weights, values, i):
    global count
    count += 1
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)

        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)

        return max(include_item, exclude_item)

def dynamic_knapsack(weight_cap, weights, values):
  global count
  number_of_items = len(weights) + 1
  all_weights = weight_cap + 1
  matrix = [ [] for _ in range(number_of_items) ]
  
  # rows are the item number, cols are weight_cap, and values are the total value for number of items and weigh_cap
  # optimal is highest weight cap and maximum number of items, i.e., bottom right of matrix
  # but i also have no clue what is going on
  for item in range(number_of_items):
    matrix[item] = [ -1 for _ in range(all_weights) ]
    for weight in range(all_weights):
      count += 1
      if item == 0 or weight == 0:
        matrix[item][weight] = 0
      elif weights[item - 1] <= weight:
        include_item = values[item - 1] + matrix[item - 1][weight - weights[item - 1]]

        exclude_item = matrix[item - 1][weight]

        matrix[item][weight] = max(include_item, exclude_item)
      else:
        matrix[item][weight] = matrix[number_of_items - 1][weight]
  return matrix[number_of_items-1][weight_cap]

weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
best_value = recursive_knapsack(weight_cap, weights, values, len(weights))
print(best_value)
print(f"Number of iterations: {count}")
count = 0
best_value = dynamic_knapsack(weight_cap, weights, values)
print(best_value)
print(f"Number of iterations: {count}")
