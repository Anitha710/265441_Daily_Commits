def my_fun():
    print("spam")
    print("spam")
    print("spam")
my_fun()

#use of return
def max(x, y):
    if x>=y:
        return x
    else:
        return y
print(max(9, 12))
z= max(17, 5)
print(z)
# Docstrings

def shout(word):
    """
    print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout("spam")

# Modules

import random
for i in range(5):
    value = random.randint(1,6)
    print(value)

#example
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))
