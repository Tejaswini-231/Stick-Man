print("Hello There!")
print("Today we are going to play HANGMAN GAME !!!")
print("If you can guess the letters in the word given...\n Here you go")
word='devsnest'
disp=['_' for _ in word]
chance=5
print(disp)
end=False
while not end:
  guess=input("Enter your guess:").lower()
  for pos in range(len(word)):
    letter=word[pos]
    if letter==guess:
      disp[pos]=guess
  print(disp)
  if guess not in word:
    chance-=1
    print("You have",chance,"guesses left!")
  if chance==0:
      end=True
      print("You have run out of guesses!")
      print('The word is ',word)
  if '_' not in disp:
      print("You have won!")
      print("The word is ",word)
      end=True
print("Thanks for Your Visit!!")
print("Run again to play again!!!")