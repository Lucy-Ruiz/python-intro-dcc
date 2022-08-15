
#Task 1 reversed string
# 1. Create a variable that saves the input of a user
# 2. Create a variable to save and execute the reversed code
# 3. Create and empty string to pass the reversed result to .join()
# 4. Apply reversed to variable that contains the input
# 5. Print variable that contains the reversed result

enter_greeting = (input('Enter a greeting: '))
word_to_reverse = ''.join(reversed(enter_greeting))
print(word_to_reverse)
for letter in reversed(enter_greeting):
    print(letter)

#Task 2 capitalized letter
# 1. Create a variable to save the input of the user
# 2. Create a variable to save the capitalized input
# 3. Apply .title() to the input
# 4. Print the variable that has the capitalized result

enter_words_to_cap = (input('Enter a word: '))
cap_word = (enter_words_to_cap.title())
print(cap_word.title())


