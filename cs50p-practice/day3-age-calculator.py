import datetime

# Ask user for their birth year
birth_year = input('What is your birth year? ')
# Calculate their age (2025 - birth_year)
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)
# Print: "You are [age] years old!"
age_in_months = age * 12
print(f'You are {age} years old and {age_in_months} months old')
# Bonus: Tell them their age in months
