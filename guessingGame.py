import random
number = random.randint(1,9)
chances = 0
print("guess the number between 1 and 9")
while chances < 5:
    guess = int(input("enter your guess"))
    if (guess == number):
        print("Congratulations you won!")
        break
    elif (guess < number):
        print("your guess was too low .pls guess a higher number",guess)
    else:
        print('your guess was too high so guess a number lower',guess)
    chances = chances + 1
if (chances > 5):
    print('you lose the number is ',guess)        