import random
i=0
userScore=0
compScore=0

print("Hi there ^_^ !")
while(i<3):
	print("\n")
	userInput = input("Choose your weapon: [R]ock, [P]aper, or [S]cissors:")
	choices = ['R', 'S', 'P']
	computerChoice = random.choice(choices)
	if(userInput == computerChoice):
		print("It appears we have a tie!")
		i=i+1
	elif(userInput =='R' and computerChoice == 'P'):
		print("You chose Rock and I chose Paper. I win!")
		i=i+1
		compScore+=1
	elif(userInput =='R' and computerChoice == 'S'):
		print("You chose Rock and I chose Scissors. You win!")
		i=i+1
		userScore+=1
	elif(userInput =='P' and computerChoice == 'S'):
		print("You chose Paper and I chose Scissors. I win!")
		i=i+1
		compScore+=1
	elif(userInput =='P' and computerChoice == 'R'):
		print("You chose Paper and I chose Rock. You win!")
		i=i+1
		userScore+=1
	elif(userInput =='S' and computerChoice == 'R'):
		print("You chose Scissors and I chose Rock. I win!")
		i=i+1
		compScore+=1
	elif(userInput =='S' and computerChoice == 'P'):
		print("You chose Scissors and I chose Paper. You win!")
		i=i+1
		userScore+=1
	else:
		print("Invalid Input. Choose again.")

print("\n")
finalScoreString = "The score is User:{} and Computer:{}".format(userScore,compScore)
print(finalScoreString)
if(userScore==compScore):
	print("We tied for the matches. Good game.")
elif(userScore>compScore):
	print("You won the bout. Congratulations!")
elif(userScore<compScore):
	print("I won the bout. Try again!")