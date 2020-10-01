
def password_checker():
    username = input('what is your username?')
    password = input('what is your password?')

    password_length = len(password)
    password_hidden = '*' * password_length

    if password_length <= 4:
        print(f'Sorry {username}. your password, {password_hidden} is too small!')
    else:
        print(f'Hey {username}, your password, {password_hidden} is {password_length} letters long.')

def age_checker():
    birth_year = input('when year were you born?')

    age = 2020 - int(birth_year)

    if age in range(1, 10):
        print(f'You are {age} years old. you\'re still very young!')
    elif age in range(11, 18):
        print(f'You are {age} years old. you\'re still a teenager!')
    elif age in range(19, 29):
        print(f'You are {age} years old. you\'re an adult now!')
    else:
        print(f'You are {age} years old. you\'re very old now!')

what_function = input('what funtion do you want to use? password checker, or age checker?')
if what_function == 'password checker':
    password_checker()
elif what_function == 'age checker':
    age_checker()
else:
   print('this function does not exist')


