hangman_diagrams = [
    """
  +---+
      |
      |
      |
     ===""", """
  +---+
  O   |
      |
      |
     ===""", """
  +---+
  O   |
  |   |
      |
     ===""", """
  +---+
  O   |
 /|   |
      |
     ===""", """
  +---+
  O   |
 /|\  |
      |
     ===""", """
  +---+
  O   |
 /|\  |
 /    |
     ===""", """
  +---+
  O   |
 /|\  |
 / \  |
     ==="""
]

print("Hello There!")
print("Today we are going to play HANGMAN GAME !!!")
print("If you can guess the letters in the word given...\n Here you go")
word = 'devsnest'
guessed = set()
disp = ['_' for _ in word]
chance = 7

print(disp)

while chance > 0:
  guess = input("Enter your guess:").lower()
  if not guess.isalpha() or len(guess) != 1:
    print("Please enter only a single alphabetical character!")
    continue
  if guess in guessed:
    print("You've already guessed that letter!")
    continue

  guessed.add(guess)

  if guess in word:
    for pos in range(len(word)):
      if word[pos] == guess:
        disp[pos] = guess
    print(disp)
  else:
    chance -= 1
    print("You have", chance, "guesses left!")
    #print(hangman_diagrams[chance - 1])
    print(hangman_diagrams[len(hangman_diagrams) - chance - 1])

  if '_' not in disp:
    print("You have won!")
    print("The word is", word)
    break

  if chance == 0:
    print("You have run out of guesses!")
    print('The word is', word)
    break

print("Thanks for Your Visit!!")
print("Run again to play again!!!")
