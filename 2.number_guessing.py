import random

top_of_range = input("Please type a max range number you want to guess: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
num_guess = 0

while True:
    num_guess += 1

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("Congratulation!")
        break
    elif user_guess > random_number:
        print('Please guess lower')
    else:
        print('Please guess higher!')

print("You got it in", num_guess, "guesses")