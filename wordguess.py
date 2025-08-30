import random
from random_word import RandomWords

words=RandomWords()
word=words.get_random_word()

attempts=10
#print(word)

guessed_word=['_']*len(word)
#print(guessed_word)

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessed_word))
  guess=input("guess a letter  ").lower()

  if guess in guessed_word:
     print("You've already guessed that letter!")
     continue

  
  if guess in word:
    for i in range(len(word)):
       if word[i] == guess:
          guessed_word[i] = guess
          print('Great guess!')
  else:
    attempts-=1
    print("attempts left ",attempts)
  if '_' not in guessed_word:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

  if attempts == 0 and '_' in guessed_word:
    print('\nYou\'ve run out of attempts! The word was: ' + word)    
    break    
    
  