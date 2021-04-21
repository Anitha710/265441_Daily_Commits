#while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1
# break
i = 0
while True:
    print(i)
    i = i + 1
    if i>= 5:
        print("Breaking")
        break

print("Finished")
# continue
z = 1
while z<= 5:
    print(z)
    z+=1
    if z == 3:
        print("skipping 3")
        continue
# for
words = ["hello", "world", "spam", "eggs"]
for x in words:
    print(x + "!")

# for loop to iterate over strings
str = "testing for loops"
count = 0
for y in str:
    if(x == 't'):
        count +=1
print(count)
# range()
numbers = list(range(3, 10))
print(numbers)
# range intervals
numbers = list(range(5, 20, 2))
print(numbers)
# example
for i in range(5):
    print("hello!")
# example
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

for a in range(10):
  if not a % 2 == 0:
    print(a+1)
while False:
  print("Looping...")