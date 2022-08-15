favorite_number = 3

import random
random.random()
random_number = random.randrange(10)
print(random_number)
numbers_away = (random_number - favorite_number)
print(f'Your favorite number was {numbers_away} numbers away')