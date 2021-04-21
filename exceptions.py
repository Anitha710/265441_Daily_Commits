try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Donr calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")

# example 1
try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

# example 2
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")
# example 3
try:
  print(1)
except:
  print(2)
finally:
  print(3)
# asserts
print(0)
assert "h" != "w"
print (1)
assert False
print(2)
assert True
print(3)
