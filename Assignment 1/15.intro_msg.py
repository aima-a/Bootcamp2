'''First, assign your name into name variable, your last name into last_name variable and your age into age
variable. Then print on the screen the following text:
Mick Jagger is 71 years old
Of course name, last name and age have to contain your information.'''

first_name = 'Aima'
last_name = 'Anwar'
my_age = 22

def intro_message(fname, lname, age):
    return print(f'{fname} {lname} is {age} years old.')

intro_message(first_name, last_name, my_age)
