'''Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
and print out the converted temperature'''

def celsius_to_fahrenheit():
    temp = float(input('Enter a Celsius temperature you would like to convert to Fahrenheit: '))
    celsius_conv = (temp * 9/5) + 32
    print(f'{temp} degrees Celsius is equal to {celsius_conv} degrees Fahrenheit')

celsius_to_fahrenheit()
