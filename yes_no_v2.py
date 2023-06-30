played_before = ""
while played_before.lower() != "xxx":
  # Ask the user if they have played before
  played_before = input("Have you played the game before?").lower()
  
  # If they say yes, output 'program continues'
  if played_before == "yes" or played_before == "y":
    played_before = "yes"
    print("Program continues")
  
  # If they say no, output 'display instructions'
  elif played_before == "no" or played_before == "n":
    print("Display instructions")
       
  else:
    print("Please answer yes / no")
    
    print("You chose {}".format(played_before))
  
