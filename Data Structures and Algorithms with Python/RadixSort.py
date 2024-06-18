def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)
      digits[digit].append(number)


    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

my_arr = [1, 4, 5, 22, 0, 1, 1, 90, 344, 209]
sorted_arr = radix_sort(my_arr)
print(my_arr)
print(sorted_arr)