import random

recont_searches = []

isـruning = True
rand = random.randint(1, 100)

while isـruning:
    num = int(input("please enter a number between 1 to 100: "))

    if num > rand:
        recont_searches.append(num)
        print("your number is high from random number")

    elif num < rand:
        recont_searches.append(num)
        print("your number is smaller to random number")

    else:
        recont_searches.append(num)
        print("Correct! You guessed the number ")
        isـruning = False

lenlist = len(recont_searches)

print(recont_searches)
print(f"the length of your list are {lenlist}")