friends = ["anitha", "kushala", "Divya", "Dharani"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends)
#2nd example
empty_list = [2,]
print(empty_list)
# 3rd example
number = 3
things = ["string", 0, [1,2,number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
# 4th example
str = "Hello World!"
print(str[8])
# reassining the list
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
# addidtion and multiplication of lists
print(nums + [4, 5, 6, 7])
print(nums * 3)
# To check if an item is in a list, the in operator can be used.
words = ["spam", "eggs", "spam", "tomato"]
print("spam" in words)
print("eggs" in words)
print("sausage" in words)
# To check if an item is not in a list, using not operator
print(not 4 in nums)
print(4 not in nums)
print(not 7 in nums)
print(7 not in nums)
# append method
nums.append(9)
print(nums)
print(len(nums))
#use of insert()
index = 1
friends.insert(index, "edwin")
print(friends)
# index() finds 1st occurrence of a list item
letters = ['p', 'q', 'r', 's', 'p']
print(letters.index('r'))
print(letters.index('p'))