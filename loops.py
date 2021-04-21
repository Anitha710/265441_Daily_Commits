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