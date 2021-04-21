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

# example pgm
try:
  print(1)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)