# Program start 

# Miles to kilometer converter func
# In mind 1 mile == 1.61 km

import os
import getpass

# Miles to kilometers
def mile_to_km(mile):
    res = float(mile) * 1.61
    print(mile, 'miles =', round(res, 2), 'kilometers')


# Ksh to US Dollars
# In mind 1ksh = 109.80 USD
def ksh_to_usd(ksh):
    res = float(ksh) * 109.80
    print(ksh, 'Kenyan shilings =', round(res, 2), 'US Dollars')

# Percent to letter grade
def percent_to_letter_grade(percent):
    p = int(percent)
    if p >= 80 and p <= 100:
        print(str(p) + '%', '=', 'A')
    # if percent in range(80, 100):
    #     print(str(percent) + '%', '=', 'A')
    elif p >= 70 and p < 80:
        print(str(p) + '%', '=', 'B')

    elif p >= 60 and p < 70:
        print(str(p) + '%', '=', 'C')

    elif p >= 50 and p < 60:
        print(str(p) + '%', '=', 'D')

    elif p >= 20 and p < 40:
        print(str(p) + '%', '=', 'E')

    elif p >= 0 and p < 20:
        print(str(p) + '%', '=', 'F')

# Kilograms into pounds(lbs)
# 1 kg == 2.20 lbs
def kg_to_lbs(kg):
    res = float(kg) * 2.20
    print(kg, 'kilograms is', round(kg, 2),'Pounds(lbs)')

# Centimeter into inches
# 1cm == 0.393701 inches
def cm_to_inches(centimeter):
    inches = 0.393701
    res = float(centimeter) * inches
    print(centimeter + ' centimeters is', res, 'Inches')





name = input('What is your name?: ').capitalize()

print('Hello',name+',','Welcome to your personal unit converter.')

# choice = input('Please choose which conversion you would like to perform:\n'
# '1 - Convert miles into kilometers\n'
# '2 - Convert Kenyan shilings into US Dollars\n'
# '3 - Convert percent to letter grade\n'
# '4 - Convert kilograms into pounds(lbs\n'
# '5 - Convert centimeters into inches\n'
# )

print('Please choose which conversion you would like to perform:\n'
'1 - Convert miles into kilometers\n'
'2 - Convert Kenyan shilings into US Dollars\n'
'3 - Convert percent to letter grade\n'
'4 - Convert kilograms into pounds(lbs\n'
'5 - Convert centimeters into inches\n')


choice = input('Choice: ')

if choice == str(1):
    mile = input("Value in miles to convert in km: ")
    mile_to_km(mile)

elif choice == str(2):
    ksh = input("Value in Kenyan shilings to convert in US Dollars: ")
    ksh_to_usd(ksh)

elif choice == str(3):
    percent = input('Percent to convert to letter grade: ')
    percent_to_letter_grade(percent)

elif choice == str(4):
    kilograms = input('Value in Kilograms to convert into pounds(lbs): ')
    kg_to_lbs(kilograms)

elif choice == str(5):
    cm = input('Value in centimeters to convert into inches: ')
    cm_to_inches(cm)

print('Goodbye', name)
