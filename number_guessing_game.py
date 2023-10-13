#guess the number game
import random

repeat = True

while repeat:
  number = random.randint(1, 100)
  guess = 0
  tries = []
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
  #print(number) #only for developer

  while guess != number:
    guess = int(input("Guess the number: "))
    if guess < number:
      print("Try higher number: ")
    elif guess > number:
      print("Try lower number: ")
    tries.append(guess)
  else:
    if len(tries) < 4:
      print(f"Nice! You guessed {number} after {len(tries)} tries!")
    elif len(tries) < 7:
      print(f"Not bad! You guessed {number} after {len(tries)} tries!")
    else:
      print(f"Damn! You guessed {number} only after {len(tries)} tries!")
  
    print(f"Here's your guessing history: {tries}")

    sum_of_difference = 0

    for t in tries:
      sum_of_difference += abs(t - number)

    print(f"Average difference was {sum_of_difference/len(tries)}")

    response = str(input("Wanna play again? y/n: "))
    if response == "y":
        repeat = True
    elif response == "n":
      print("Thanks for playing!")
      repeat = False
    else:
      print("Error. You fucked up in 1 letter typing")
      repeat = False
