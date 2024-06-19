memo = {}
def fib(num):
    if num <= 1:
        return num
    if num in memo:
        return memo[num]
    answer = fib(num-1) + fib(num-2)
    memo[num] = answer
    return answer

print(fib(20))