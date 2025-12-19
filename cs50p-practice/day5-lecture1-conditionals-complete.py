# Grade calculator based on an input
score = int(input('Score: '))

if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Grade: F')

# Compare integers
x = int(input('What is x? '))
y = int(input('What is y? '))

if x < y or x > y:
    print('x is not equal to y')
else:
    print('x is equal to y')

# Determine if an integer is even or odd by defining a function
def main():
    x = int(input('What is x? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    return n % 2 == 0

main()

# Checking if a name tallies with a house
name = input('What is your name? ')

match name:
    case 'Harry' | 'Hermoine' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')
