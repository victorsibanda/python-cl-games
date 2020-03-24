# Mega fizz buzz exercise
# this exercise has 4 versions

# Boring Buzz
# The point of the game is to count up to a number and whenever we get multiples of 3 you will respond with 'boring' and multiples of 5 you'll respond with 'buzz'.
# multiples of 3 and 5 youll respond with 'boringbuzz'
# do this exercise with while loop and if functions.

#specs:
# multiples of 3 -- > boring
# multiples of 5 -- > buzz
# multiples of 3 and 5 --> boringbuzz


# then do this functionally




from exercise_fizz_buzz_functions import *

while True:

    num = int(input('What range do you want to check?'))
    for i in range (1, num+1):
        print(fizz_buzz(i))






