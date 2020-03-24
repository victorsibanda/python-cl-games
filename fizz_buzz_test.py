from exercise_fizz_buzz_functions import *

print('is is_divisible(10,5) should be equal to buzz')
print(is_divisible(10,5) == 'buzz')
print ('Got:', is_divisible(10,5) )
#Should return True

print('is is_divisible(9,3) should be equal to buzz')
print(is_divisible(9,3) == 'boring')
print ('Got:', is_divisible(9,3) )
#Should return True

print('is is_divisible(20,3) should be equal to none')
print(is_divisible(20,3) == 'boring')
print ('Got:', is_divisible(20,3) )
#Should return False

print('is boringbuzz(15) should be equal to boringbuzz')
print(boringbuzz(15) == 'boringbuzz')
print ('Got:', boringbuzz(15))

print('is boringbuzz(35) should be equal to none')
print(boringbuzz(35) == 'boringbuzz')
print ('Got:', boringbuzz(35))
