
def fizz_buzz(num):
    if boringbuzz(num):
        return "boringbuzz" , num
    elif is_divisible(num,3):
        return 'boring' , num
    elif is_divisible(num,5):
        return 'buzz', num
    else:
        return num


def boringbuzz(num) :
    if is_divisible(num,3) and is_divisible(num,5):
        return ("boringbuzz")


def is_divisible(num,mod):
    if mod == 3 and num % mod == 0 :
        return 'boring'
    elif mod == 5 and num % mod == 0:
        return 'buzz'




