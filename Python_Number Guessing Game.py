import random

no_of_guesses = 1
print("\nNote :- You have 10 attempts to guess the number.\n ")
random_number = random.randint(1 , 100)

while (no_of_guesses<=10) :
    guessed_number = int(input("Guess the number from 1 to 100 : "))
    if guessed_number<random_number :
        print("Greater Number Please...")
    elif guessed_number>random_number :
        print("Smaller Number Please...")
    else :
        print("\n******* You Won","\U0001F60A","*******")
        print("You guessed the number in" , no_of_guesses , "attempts.\n")
        break
    print("Number of guesses left :", 10-no_of_guesses , "\n")
    no_of_guesses = no_of_guesses + 1

if(no_of_guesses>10) :
    print("******* Game Over *******")
    print("****** You Lose","\U0001F614","******")