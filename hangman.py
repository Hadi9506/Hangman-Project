import random
Rounds = 1
Score = 0
Animals = ['dog','cow','horse','donkey','tiger']
Months = ['january','february','march','april','may','june']
Adjectives = ['proud','first','great','quiet','small']
Names = ['peter','jake','kevin','zach','josh']
print ('Word list is','\n',
       '1.Animals: ','\n',
       '2.Months: ','\n',
       '3.Adjectives: ','\n',
       '4.Names: ')

def hangman (tries):
    Stages = ["""
           ____
          |    |
          |    O
          |   /|\\
          |    |
          |   / \\
          |
        ========
        """, """
           ____
          |    |
          |    O
          |   /|\\
          |    
          |    
          |
        ========
        ""","""
           ____
          |    |
          |    O
          |    |
          |    
          |    
          |
        ========
        """,     """
           ____
          |    |
          |    
          |    
          |    
          |    
          |
        ========
        """]
    return Stages[tries]
def Answer ():      #Answer Function

        while True:     #loop to take input and check if input is right 
            Words = input ('Select from the lists given above.''\n'
                        'Select List: ')
    
            if Words in ['1','2','3','4']:
                break
    
            else:
                print ('Invalid list no. Please enter 1,2,3,4' )
    
        if Words == '1':
            return random.choice (Animals)
        
        elif Words == '2':
            return random.choice (Months)
        
        elif Words == '3':
            return random.choice (Adjectives)
        
        elif Words == '4':
            return random.choice (Names)
        
while Rounds > 0:   #Main Loop   
    Hints = 1
    Answer_Word = list(Answer())
    Allowed_guess = []
    Allowed_guess.extend(Answer_Word)
    Guessed_letters = []  
    Updated_Word = ['_' for _ in range(len(Answer_Word))]
    tries = 3
    print ('Guess the word',' ' .join(Updated_Word))

    while Updated_Word != Answer_Word  and tries > 0 : #loop which runs the round
        
        print (hangman(tries))
        Guess = input ('enter an alphabet: ').lower()
    
        if Guess in Guessed_letters :
            print ('You have already guessed this letter')
            continue
        
        if len(Guess) != 1 or not Guess.isalpha():
            print ('Input is not accepted, enter a single alphabet')
            continue
    
        Guessed_letters.append(Guess)
        correct_guess = False
    
        for i in range(len(Answer_Word)):
        
            if Guess == Answer_Word[i]:
                Updated_Word[i] = Guess
                Allowed_guess.remove(Guess)
                correct_guess = True
            
        print ('The remaining word is',' ' .join(Updated_Word))
    
        if not correct_guess:
            tries -= 1
            print ('incorrect guess, ',tries,'tries remain.')
            
            while Hints == 1 and tries != 0 :
                
                Hint_choice = input ('If you want a hint press enter.''\n'
                                 'Else press any key and enter.''\n''')         #obtaining a hint if user wants
                
                if Hint_choice == '':
                    print (f'The answer contains the letter {random.choice(Allowed_guess)}')
                    Hints = 0
                    
                else:
                    break
                
        print ('The letters used are',' '.join(Guessed_letters))
                 
        if Updated_Word == Answer_Word:
            print ('Congrats you guessed the answer',"".join(Answer_Word))
            Score += 1
            break 
    
    if tries == 0:      #Result determination and transition to next round
        print (hangman(tries))
        print ('You failed to guess the answer, correct answer was',"".join(Answer_Word))
        
    Enter = input ('To start next round press enter''\n''To exit press another key and enter: ')
    
    if Enter == '':       #input to start next round or end game
        print ('Next round is starting')

    else :
        Rounds = 0

print ('Thanks for playing''\n'f'Your score is {Score} ')