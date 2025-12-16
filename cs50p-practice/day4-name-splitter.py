# Name Splitter - Day 4 Practice

# Ask user for their full name (first and last)
full_name = input("What's your full name? ")

# Split the name into parts
parts = full_name.split()
first = parts[0]
last = parts[1]

# Use .split() method (it splits at spaces)

# Print first name
print(f'First name: {first}')
      
# Print last name
print(f'Last name: {last}')
# Bonus: Print in reverse order (Last, First)
print(f'Reverse order: {last}, {first}')
