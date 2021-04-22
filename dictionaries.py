# dictionaries
ages = {"Dave": 24, "Mary":42, "Jhon": 58}
print(ages["Dave"])
print(ages["Mary"])
# use of get
pairs = { 1: "apple", "orange": [2, 3, 4],
          True: False,
          None: "True",
          }
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))\
#example
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(7, 5) + fib.get(4, 0))
# tuple
words = ("spam", "eggs", "sausages",)
print(words[0])
# list slices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[:6])
print(squares[::6])
print(squares[2:6:3])
# example
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])