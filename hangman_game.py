import random
from hangman_list import word_list
from hangman_art import stages, logo

choose_word=random.choice(word_list)

lives=6
display=[]

for i in choose_word:
    display.append("_")

print(logo)

print(display) 

end_game=False
while not end_game:
    
    guess=input("guess the letter :").lower()
    
    if guess in display:
        print(f"already guess this letter {guess}")
    
    for i in range(len(choose_word)):
        letter=choose_word[i]
        if letter == guess:
            display[i]=letter
            print(display)
            
    if guess not in choose_word:
        print(f"You have guess {guess}, which is not in the word. Therefore you lose a life")
        lives-=1
        if lives==0:
            end_game=True
            print("You lose,game over")
            print(f"The correct word is {choose_word}")
    
    if "_" not in display:
        end_game=True
        print("You win")
    
    print(stages[lives])