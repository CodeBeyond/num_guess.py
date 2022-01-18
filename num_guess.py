print("Enter a number for a player to guess.")
num = int(input())
print(num)
print("Enter a guess.")
numbers_guessed = 0
while numbers_guessed < 99999999999999999999999999999999999999999999999999999999999999:
    guess = int(input())
    numbers_guessed = numbers_guessed + 1
    if guess < num:
        print("Too low - try again.")
    elif guess > num:
        print("Too high - try again.")
    else:
        if guess == num:
            print("You guessed in ", numbers_guessed, "tries.")
        break
