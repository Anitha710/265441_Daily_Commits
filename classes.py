class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)

#example
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()

# example 2
class A:
    def a(self):
        print(1)


class B(A):
    def a(self):
        print(2)


class C(B):
    def c(self):
        print(3)


c = C()
c.a()
# Regular Expressions
import re
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No Match")
# replacing string
import re
str = "My name is Anitha. Hi Anitha"
pattern = r"Anitha"
newstr = re.sub(pattern, "AMY", str)
print(newstr)

#groups
import re
pattern = r"eggs(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")

#tuple unpacking

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# ternary operator
x = 7
y = 1 if x >= 5 else 42
print(y)
z = 1 if 2+2 == 5 else 2
print(z)

#example
for i in range(10):
   if i > 5:
      print(i)
      break
else:
   print("7")

#example
try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)
# example
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)
# example
for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)