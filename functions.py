# Example function:
def display_name(name):
    print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


display_name('Mike')
display_name('Ian')
display_name('Nevin')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2


def add_one_to_number(number):
    number_one = 1
    add_one = number + number_one
    return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


result = add_one_to_number(30)

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value

# Problem 1
# Write a function that takes in two numbers
# The logic of the function should add those two numbers together and return a sum
# Capture the returned value in a variable and print it to the console

def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)
    return total

add_two_numbers(5,7)
add_two_numbers(3.14, 451.17)
add_two_numbers(9749, 1)

# Problem 2
# Write a function that takes in two strings
# The logic of the function should concatenate those two strings together and return the concatenated result
# Capture the returned value in a variable and print it to the console

def write_two_strings(string1, string2):
    phrase = string1 + ' ' + string2
    print(phrase)
    return phrase

phrase1 = write_two_strings('Seattle', 'is the evergreen state')
write_two_strings('Python is:', 'my favorite programing language')
write_two_strings('Tea and cookies', 'are the best combination')

# Problem 3
# Write a function that takes in a string
# The logic of the function should print each character of the string one at a time to the console
# HINT: for loop is one way to do this


def separating_string(string_to_divide):
    for character in string_to_divide:
        print(character)
        

separating_string('Lake Michigan')
separating_string('Lake Union')
separating_string('West Coast')


# Problem 4
# Write a function that takes in a string
# The logic of the function should print the string to the console but only if that string has three or more characters in it
# If it is less than three characters, then print to the console 'we need a larger string to print!'

def l_string(string1):
    if len(string1) >= 3:
        print(string1)
    elif len(string1) < 3:
        print('We need a larger string to print')

l_string('it')
l_string('lettuce')

#Task 1 String manipulation

def team_characters(team):
    for character in team:
        print(team[0] + team[-1])
        return(team)

team_characters('Packers')

#Task 2 

def numbers_100():
    for number in range(101):
        if number % 3 == 0 and number % 5 == 0:
            print('peanut butter jelly')
        elif number % 3 == 0:
            print('peanut butter')
        elif number % 5 == 0:
            print('jelly')
        else:
            print(number)
            

numbers_100()

#Task 3 word-letter indexing
