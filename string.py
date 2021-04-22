# String Formatting
print("{0}{1}{0}".format("abra", "cad"))
# example
a = "{x}, {y}".format(x=5, y=12)
print(a)
# example
str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)
# numeric expression
a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
# list functions
nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)
#example
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
# example 2
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))
# function
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y - 1)


print(power(2, 3))
