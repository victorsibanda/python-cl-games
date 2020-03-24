# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')
user_input = str(input('Mr Miyagi..\n'))

while user_input != 'Sensei, I am at peace':

    user_input = str(input('What do you want to say?'))

    if '?' in user_input and 'Sensei' not in user_input:
        print('You are smart, but not wise - address me as Sensei please')
    elif '?' in user_input:
        print('questions are wise, but for now. Wax on, and Wax off!')
    elif 'block' in user_input or 'blocking' in user_input:
        print('Remember, the best block, is to not to be there')
    else:
        print('do not lose focus. Wax on. Wax off.')

print('Sometimes, what heart know, head forget')
