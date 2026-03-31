import random # import random module


# while loop to keep the game running
while True:
 
 
# Ask the user if they want to roll the dice 
 user = input('Roll the dice🎲?(yes/no)').lower()


 # Generate a random number between 1 to 6 
 computer = random.randint(1,6)


#If  the user types "yes" rolled the dice  
 if user == 'yes':
    print('You rolled:',computer)


#If the  user types "no" print okay maybe next time
 elif user == 'no':
   print('Okay! maybe next time')


#If  the user types invalid text print please type "yes or no"    
 else:
   print(f'Please type "yes" or "no". ')
   continue
 

# Ask if  the user wants to play another round 
 answer = input('Do you want to play another round (yes/no):').lower()

 
# If answer "no" print thanks for playing and break the loop
 if answer == 'no':
   print('Thank you for playing') 
   break  













































