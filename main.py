# Joshua Phillips
# 11/21/24
# Menu math :)

import time
import math



def calculate_cricle_area(radius):
    area = math.pi * radius**2
    return area

def calculate_power(base, exponent):
    result = base**exponent
    return result

def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

def display_menu():
    print('Menu:')
    print('1. Calculate area of a circle')
    print('2. Raise a number to a power')
    print('3. Calculate area of a right triangle')
    print('4. Exit')

def main():
    while True:
        display_menu()
        choice = int(input('Pick what to calculate(1-4): '))
        if choice == 1 :
            radius = int(input('Enter the radiuse of your circle: '))
            area = calculate_cricle_area(radius)
            print(f'The area of the circle is: {area} sq. ft.')
        elif choice == 2:
            base = int(input('Enter the base: '))
            exponent = int(input('Enter the exponent: '))
            result = calculate_power(base, exponent)
            print(f'The number {base} raised to the power of {exponent} is: {result}.')
        elif choice == 3:
            base = int(input('Enter the base: '))
            height = int(input('Enter the height: '))
            area = calculate_triangle_area(base, height)
            print(f'The area of the right triangle is: {area}')
        elif choice == 4:
            print('Exiting script...')
            time.sleep(2)
            print('Thank you for using my script today!')
            time.sleep(2)
            break
        else:
            print('Invalid input, number only!(1-4)')

if __name__ == '__main__':
    main()
