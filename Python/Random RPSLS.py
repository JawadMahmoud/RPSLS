import random

## Checks whether the input from the user is incorrect
def incorrect_input(choice):
    answers = ["rock", "paper", "scissors", "lizard", "spock"]
    return choice not in answers

## Generates a random move in response to the user's move
def gen_random_answer():
    answers = ["rock", "paper", "scissors", "lizard", "spock"]
    pick = random.choice(answers)
    return pick

## Calculates the result, 0 -> same symbols, 1 -> human wins, -1 -> computer wins
def result(humanChoice, compChoice):
    if humanChoice == compChoice:
        return 0

    return {
        "rock" : {
            "lizard" : 1,
            "scissors" : 1,
        },
        "paper" : {
            "rock" : 1,
            "spock" : 1,
        },
        "scissors" : {
            "paper" : 1,
            "lizard" : 1,
        },
        "lizard" : {
            "paper" : 1,
            "spock" : 1,
        },
        "spock" : {
            "rock" : 1,
            "scissors" : 1,
        }
    }.get(humanChoice).get(compChoice, -1)

## Keeps requesting an input of number of rounds to play until valid input provided
while True:
    rounds = int(input("How many rounds would you like to play? (Max 25)"))
    if rounds > 0:
        break
    else:
        print("Please choose number of rounds from 1-25")

currentRound = 1
humanScore = 0
compScore = 0

## Repeats until all rounds played
while currentRound <= rounds:
    choice = input("\nChoose:\n (rock, paper, scissors, lizard, spock)\n")
    choice = choice.lower()
    if incorrect_input(choice):
        print("\nKindly use a correct symbol from:\n (rock, paper, scissors, lizard, spock)\n")
        continue
    
    pick = gen_random_answer()

    roundResult = result(choice, pick)
    
    print("\n You Chose: " + choice + " | Computer chose: " + pick + "\n")
    if roundResult == 0:
        print("Draw")
    elif roundResult == 1:
        print("You Win this Round Human!")
        humanScore += 1
    else:
        print("You Lose the Round! *evil laugh*")
        compScore += 1

    print("\n Your Score: " + str(humanScore) + " | Computer score: " + str(compScore) + "\n")
    currentRound += 1

## Shows final result to user
if humanScore > compScore:
    print("You beat me Human, you are the superior being.")
elif humanScore < compScore:
    print("No Human can beat me!")
else:
    print("We Drew. So what now..?")