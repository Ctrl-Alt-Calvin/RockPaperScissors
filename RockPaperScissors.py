import random
def main():
    options = ["Rock", "Paper", "Scissors"]
    botChoice = random.choice(options).lower()
    userInput = input("Rock, Paper, or Scissors? ").lower()
    while userInput == "rock" or userInput == "paper" or userInput == "scissors":
        if userInput == "rock" and botChoice == "scissors":
            print("I pick", botChoice)
            print("You Win!")
            main()
        elif userInput == "rock" and botChoice == "paper":
            print("I pick", botChoice)
            print("You Lost!")
            main()
        elif userInput == "scissors" and botChoice == "paper":
            print("I pick", botChoice)
            print("You Win!")
            main()
        elif userInput == "scissors" and botChoice == "rock":
            print("I pick", botChoice)
            print("You Lost!")
            main()
        elif userInput == "paper" and botChoice == "rock":
            print("I pick", botChoice)
            print("You Win!")
            main()
        elif userInput == "paper" and botChoice == "scissors":
            print("I pick", botChoice)
            print("You Lost!")
            main()
        else:
            print("I pick", botChoice)
            print("It's a tie!")
            main()
    else:
        print("Please choose Rock, Paper, Scissors!")
        main()
main()
