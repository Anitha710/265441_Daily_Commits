print(2 == 3)
print("hello" == "hello")
print("eleven" != "seven")
print(10 < 10)
print(7 > 7.0)
print(9 >= 9.0)
print(8.7 <= 8.70)
if 10 > 5:
    print("10 is greater than 5")
x = 7
if x > 3:
    print("3")
    if x < 5:
        print("5")
        if x == 7:
            print("7")

if not True:
  print("1")
elif not(1 + 1 == 3):
  print("2")
else:
    print("3")

if 1+1*3 == 6:
    print("yes")
else:
    print("no")
x = 4
y = 2
if not 1+1 == y or x == 4 and 7==8:
    print("yes")
elif x>y:
    print("no")