# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.

while True:

    user_q = str(input('What is the rating?'))

    ratings = {'universal':'everyone can watch',
           'pg': 'General viewing, but some scenes may be unsuitable for young children',
           '12': 'Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.',
           '15':'No one younger than 15 may see a 15 film in a cinema.',
           '18': 'No one younger than 18 may see an 18 film in a cinema.'}

    if user_q == 'universal':
        print (ratings['universal'])
    elif user_q == 'pg':
        print (ratings['pg'])
    elif user_q == '12':
        print (ratings['12'])
    elif user_q == '15':
        print (ratings['15'])
    elif user_q == '18':
        print (ratings['18'])
    else:
        print ('that is not a rating please enter again. Try pg, universal, 12, 15, 18')