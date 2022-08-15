#Lab - Conditionals 

#Task 1: Driving age
legal_driving_age = 16
user_age = int(input('Enter your age: '))

if user_age >= legal_driving_age:
    print('You are legally able to drive.')
else:
    print('You are not enough to drive yet')

#Task 2: Random number

import random

random_number = random.randrange(10)
print(random_number)

if random_number == 0 or random_number == 1 or random_number == 2:
    print('0 or 1 or 2')
elif random_number == 3 or random_number == 4 or random_number == 5:
    print('3 or 4 or 5')
elif random_number == 6 or random_number == 7 or random_number == 8:
    print('6 or 7 or 8')
elif random_number == 9 or random_number == 10:
    print('9 or 10')

#Task 3: NFL teams

user_nfl_team = input('Enter your favorite NFL team: ')

if user_nfl_team == 'Bears':
    print('Quarterback much?')
elif user_nfl_team == 'Vikings':
    print('Loud noises!')
elif user_nfl_team == 'Lions':
    print('lol! They\'re bad')
elif user_nfl_team == 'Packers':
    print('Best team in the world. Actually the universe')
else:
    print('Pick a different team')