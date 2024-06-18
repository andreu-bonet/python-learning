memo = {}

def fibonacci(num):
  if num < 0:
    return
  if num == 0:
    return 0
  if num == 1:
    return 1
  if num in memo:
    return memo[num]
  memo[num] = fibonacci(num - 2) + fibonacci(num - 1)
  return fibonacci(num - 2) + fibonacci(num - 1)
  
# Test your code with calls here:
print(fibonacci(2))
print(fibonacci(100))