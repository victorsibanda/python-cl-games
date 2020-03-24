import random
# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
magic_number = random.randrange(0, 20,1)
count = 6
# I need to ask user for input
print(magic_number)

while count != 0 :
    user_number = int(input('What do you think the magic number is between 0 and 20:'))
# I need to check if this input matches a magic_number

    if user_number == magic_number and count != 0 :
        print (f'you are correct the magic number is {magic_number}')
        break
    elif user_number != magic_number and count != 0 :
        count = count - 1
        print(f'try again please you have {count} more tries')
        continue
    else:
        # if user_number != magic_number:
        print (f'sorry you failed the magic number was{magic_number}')




# I need to let the user know if the response was write or not
#self five