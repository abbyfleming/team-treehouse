import random

def game():
	# generate random number between 1 and 10
	secret_num = random.randint(1, 10)
	guesses = []

	while len(guesses) < 5:

		guess = input("Guess a number between 1 and 10: ")

		try:
			# check to make sure input is a number
			guess = int(guess)
		except ValueError:
			print("{} isn't a number!".format(guess))

		else:
			# compare guess to secret number
			if guess == secret_num:
				print("You got it! My number was {}".format(secret_num))
				break
			# print higher or lower than guess
			elif guess < secret_num:
				print("My number is higher than {}".format(guess))
			else: 
				print("My number is lower than {}".format(guess))

			# add guess to list
			guesses.append(guesses)

	else: 
		print("You didn't get it! My number was {}".format(secret_num))

	play_again = input("Do you want to play again? Y/n")

	if play_again.lower() != 'n':
		game()
	else:
		print("Bye!")

game()
