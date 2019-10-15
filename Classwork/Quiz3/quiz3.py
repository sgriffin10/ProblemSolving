"""
----------------------------------------------------------------------
Q1. complete the following function
----------------------------------------------------------------------
"""

def is_decreasing(data):
    """
    Return True if the list is currently sorted in increasing order.
    Return False otherwise
    """
    for i in range(len(data) - 1):
        if data[i] >= data[i + 1]:
            return False
    return True


# Uncomment the following lines to test
# data_1 = [2019, 15, 10]
# data_2 = [2019, 10, 15]
# data_3 = [2019, 10, 10]
# print(is_decreasing(data_1))
# print(is_decreasing(data_2))
# print(is_decreasing(data_3))

## Expected output:
## True
## False
## False


"""
----------------------------------------------------------------------
Q2. Below are all your names in a string. Please complete the function 
to run a simulation of 100 times of class cold-callings. In this 
simulation, every student has equal chance to be called. This function 
should return a dictionary that records how many times each students 
get called. Please do not change any code outside function.
----------------------------------------------------------------------
"""

import random

random.seed(42)
NAMES_STRING = 'Krishna, Emely, Demi, Gregory, Spencer, Myat, Carmen, Victoria, Jinna, Nico, Olivia, Jenny, Rachel, Shaun, Brian, David, Patrick, Shirley, Arteen, Julie'
delimiter = ', '
t = NAMES_STRING.split(delimiter)
# print(t)

def cold_call(s):
    """
    Return a dictionary of name: positive integer pairs
    """
    d = dict()
    for i in range(101):
        name = random.choice(s)
        for name in s:
            if name not in s:
                d[name] = 1
            else:
                d[name] += 1
        return d




# When you've completed your function, uncomment the
# following lines and run this file to test!


print(cold_call(t))
## Expected output:
## {'Gregory': 6, 'Krishna': 4, 'Jinna': 9, 'Victoria': 9, 'Spencer': 4, 'Shirley': 7, 'Demi': 8, 'Arteen': 4, 'Shaun': 3, 'Emely': 5, 'Carmen': 7, 'Patrick': 1, 'Julie': 4, 'Brian': 5, 'Myat': 4, 'Meiling': 5, 'Xintong': 6, 'Jenny': 6, 'Nico': 2, 'David': 1}


"""
----------------------------------------------------------------------
Q3. Please complete the following function
----------------------------------------------------------------------
"""

Expected_output = {'Gregory': 6, 'Krishna': 4, 'Jinna': 9, 'Victoria': 9, 'Spencer': 4, 'Shirley': 7, 'Demi': 8, 'Arteen': 4, 'Shaun': 3, 'Emely': 5, 'Carmen': 7, 'Patrick': 1, 'Julie': 4, 'Brian': 5, 'Myat': 4, 'Meiling': 5, 'Xintong': 6, 'Jenny': 6, 'Nico': 2, 'David': 1}

def print_hist(data):
    """
    given a dictionary of name: positive integer pairs,
    print rows with the name and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    """
    for i in sorted(data):
        asterisks = '*' * data[i]
        print('{}: {}'.format(i, asterisks))

# When you've completed your function, uncomment the
# following lines and run this file to test!

# roster_dict = Expected_output
# print_hist(roster_dict)

## Expected output:
## Gregory: ******
## Krishna: ****
## Jinna: *********
## Victoria: *********
## Spencer: ****
## Shirley: *******
## Demi: ********
## Arteen: ****
## Shaun: ***
## Emely: *****
## Carmen: *******
## Patrick: *
## Julie: ****
## Brian: *****
## Myat: ****
## Meiling: *****
## Xintong: ******
## Jenny: ******
## Nico: **
## David: *



"""
----------------------------------------------------------------------
Q4. Please complete the following function to use APIKEY to 
get current temperature (in Fahrenheit) from openweathermap.org.
If you use YOUR_OWN_APIKEY, you will get extra 10 points.
APIKEY = '8f62260aa7890d58d9a026e2810341ea'
----------------------------------------------------------------------
"""
def get_current_temp():
    """
    Return current temperature in Fahrenheit from api.openweathermap.org
    """
    pass

import urllib.request
import json

APIKEY = '68b6d3a4e115c1ccccd6c47e7a52a914'
city = (input('Please enter city: '))
country_code = (input('Please enter country code: '))
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
city_upper = city.upper()

f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)


# How do we get current temperature?

main = response_data['main']
temp = main['temp']
celsius_temp = (temp - 273.15)


print('The current temperature in', city_upper, f'is {celsius_temp:.1f} degrees celsius.')


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(get_current_temp())

## Expected output:
## Your professor is not god. He did not know what temperature would be at this moment.