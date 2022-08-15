#Loops

#Task 1: five hellos
for hello in range(5):
    print('hello')

#Task 2: counting
for number in range(11):
    print(number)

#Task 3: counting backwards
for number in range(10, -1, -1):
    print(number)

#Task 4: prompted output
times_to_print = int(input('enter a number: '))
for item in range(times_to_print):
    print('devcodecamp')

#Task 5: word split-up
team = 'packers'
for letter in team:
    print(letter)

#Task 5: fizzbuzz
for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz') 
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)

#Task 7: 5 hellos while
target = 5
counter = 0

while counter <= 5:
    counter += 1
    print('hello')

#Task 8: validation

password = '123123'
entered_password = input('Enter your password: ')

while entered_password != password:
    entered_password = input('Enter your password: ')
if entered_password == password:
    print('User validated')

