import random

x = random.randint(1, 100)
while (guess := int(input("Угадай число:"))) != x:
