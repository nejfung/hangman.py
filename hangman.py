import random

word_bank = ["owl", "brown", "buzz", "fly", "python", "fork", "potato", "tomato", "table", "bike", "elevator", "piano", "music", "jumping", "telephone", "television", "lamp", "school", "orangutan", "lemon", "dog", "fry", "neon", "orange", "strawberry", "construction", "alphabet", "soup", "korea", "earth", "jupiter", "gold", "silver", "hangman", "swimsuit", "computer", "sock", "dress", "underwear", "sink", "bathtub", "soccer", "hockey", "football", "grass", "flowers", "spork", "nail", "toe", "glasses", "clock", "wardrobe", "bathrobe", "kitchen", "donkey", "switch", "wrapper", "drapes", "stamp", "race", "hammer", "ham", "bone", "taco", "maid", "made", "door", "yam", "helpful", "difficult", "jazz", "pyjamas", "zombie", "glow", "clean", "icicle", "drawer", "lazy", "escape", "yell", "glass", "frighten", "sky", "books", "rubber", "plastic", "ocean", "bottles", "coffee", "chocolate", "chips", "yogurt", "cereal", "honest", "good", "man", "woman", "girl", "boy", "math", "science", "french", "baguette", "oysters", "number", "four", "private", "drive", "proud", "say", "perfectly", "normal", "very", "last", "people", "strange", "involved", "moustache", "thin", "blonde", "twice", "usual", "hair", "son", "daughter", "clipboard", "jungle", "desert", "sand", "beach", "homework", "housework", "wife", "money", "tax", "sleep", "blanket", "sheet", "government", "council", "vote", "elections", "doorknob", "handle", "boat", "sail", "knot", "paddle", "steer", "quiz", "game", "board", "card", "trick", "suit", "whisk", "water", "air", "plants", "animals", "ant", "few", "queen", "fox", "white", "unicorn", "ivy", "monkey", "wheelchair", "pistachio", "hummingbird", "robin", "thunder", "shoe", "show", "snow", "know", "knot", "knit"]

#choose random word from word bank
word = random.choice(word_bank)
word_list = list(word)

word_to_show = []
lives = 5

#make list with underscores to represent unknown letters
for x in range(len(word)):
    word_to_show.append("_")

print("Welcome to Hangman!")
print("".join(word_to_show))

#loop for several games
while True:

  #loop per guess in game
  while True:

      #get the guessed letter
      letter = input("Enter a letter: ")
      letter = letter.lower()

      #if it's an invalid input
      if len(letter) != 1:
        print("Please input only one letter")
      elif letter.isalpha() != True:
        print("Please enter a letter")

      #if the letter does not appear in the mystery word
      elif word.count(str(letter)) == 0:
          print("That letter in not in the mystery word")
          lives-=1

          #if the player is out of lives, quit the game loop
          if lives == 0:
            print("\nYou're out of lives :(")
            print("The mystery word was:")
            print(word + "\n")
            break

      #if the letter is in the mystery word
      else:
        #replace each underscore in word_to_show with the letter if it's in the right position
          for x in range(len(word)):
              if word_list[x] == letter:
                  word_to_show[x] = letter
          #if there's no more unknown letters
          if word_to_show.count("_") == 0:
            print(word)
            print("You win!\n")
            break
      
      #print the current known letters and lives left
      print("".join(word_to_show))
      print("Lives: " + str(lives) + "\n")

  #once the game is over, ask if the player wants to play again
  if input("Play again? y/n: ") == "y":
    #get a new random word and reset word_to_show
    word = random.choice(word_bank)
    word_list = list(word)

    word_to_show = []
    lives = 5

    for x in range(len(word)):
      word_to_show.append("_")
    print("".join(word_to_show))
  
  else:
    #end the program
    break


    