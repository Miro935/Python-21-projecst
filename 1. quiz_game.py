print("Welcome to the Miro's world ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :D")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "center processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


answer = input("What does WTO stand for? ")
if answer.lower() == "world trade organization":
    print('Correct')
    score += 1
else:
    print('Incorrect!')



answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str(score / 4 * 100) + " %.")