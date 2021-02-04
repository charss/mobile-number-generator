import random

num = '09'

for _ in range(9):
    num += str(random.randint(0, 9))

print(num)
