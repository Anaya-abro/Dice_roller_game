import random # import random module


# while loop to keep the game running
while True:
 
 
# Ask the user if they want to roll the dice 
 user = input('roll the dice🎲?(yes/no)').lower()


 # Generate a random number between 1 to 6 
 computer = random.randint(1,6)


#if  the user types "yes" rolled the dice  
 if user == 'yes':
    print('you rolled:',computer)


#if the  user types "no" print okay maybe next time
 elif user == 'no':
   print('okay! maybe next time')


#if  the user types invalid text print please type "yes or no"    
 else:
   print(f'please type "yes" or "no". ')
   continue
 

# Ask if  the user wants to play another round 
 answer = input('Do you want to play another round (yes/no):').lower()

 
# if answer "no" print thanks for playing and break the loop
 if answer == 'no':
   print('Thank you for playing') 
   break  













































