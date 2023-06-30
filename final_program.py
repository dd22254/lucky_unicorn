import random


# Functions go here...
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "yes"
      return response

    else:
      print("Please answer yes / no")


def instructions():
  print()
  statement_generator("How to Play", "#")
  print()
  statement_generator("The rules of the game go here", "~")
  print()
  print(
    "You only have 1-10 rounds to play the this game, each round you will spend $1."
  )
  print()
  print(
    "From each round you will get a donkey, a zebra, a horse and if you're lucky you will get a unicorn."
  )
  print()
  print("Here's the payout amounts...")
  print()
  print("Unicorn: $5.00, balance will increase by $4")
  print("Horse: $0.50, balance will decrease by $0.50 ")
  print("Zebra: $0.50, balance will decrease by $0.50")
  print("Donkey: $0.00, balance will decrease by $1.00")
  print()
  print(
    "Hint: Try to avoid the donkey and try to get the unicorn so your balance will increse"
  )
  return ""


# Functions go here...
def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10\n"

  valid = False
  while not valid:
    try:
      # ask the question
      response = int(input(question))

      # if the amount is too low / too high give
      if low < response <= high:
        return response

      # output an error
      else:
        print(error)

    except ValueError:
      print(error)


def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "yes":
  instructions()
print()
print("Lucky Unicorn Game Continues")
print()
statement_generator("Let's get started", "^")

# Main routine goe here
print()
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0
print()
play_again = input("Press <Enter> to play... ").lower()
while play_again == "":

  # increase # of rounds played
  rounds_played += 1
  print()
  # Print round number
  print("***** Round #{} *****".format(rounds_played))

  chosen_num = random.randint(0, 100)

  # Adjust balance
  # if the random # is between 1 and 5,
  # user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    prize_decoration = "!"
    balance += 4

  # if the random # is between 6 and 36
  # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    prize_decoration = "D"
    balance -= 1

  # The token is either a horse or zebra...
  # in both cases subtract $0.50 from the balance
  else:
    # if the number is even, set the chosen
    # item to a horse
    if chosen_num % 2 == 0:
      chosen = "horse"
      prize_decoration = "H"

    # otherwise set it to a zebra
    else:
      chosen = "zebra"
      prize_decoration = "Z"
      balance -= 0.5

  outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

  statement_generator(outcome, prize_decoration)

  if balance < 1:
    # If balance is to low, exit the game end
    # output a suitable message
    play_again = "xxx"
    print()
    statement_generator("Sorry you have run out of money", "$")
  else:
    play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
statement_generator("RESULT", "=")
print()
print("Final Balance: ${}".format(balance))
print()
statement_generator("Thank you for playing the Unicorn Game!", "+")
