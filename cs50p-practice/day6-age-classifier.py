# Ask user for their age
age = int(input('Age: '))
# Classify them:
# 0-12: Child
# 13-17: Teenager
# 18-64: Adult
# 65+: Senior
if age < 0:
    print('Invalid age, Age must be positive')
elif age > 150:
    print('Invalid age, input is too large')
elif age < 13:
    print('Child')
elif age < 18:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('Senior')

# Print the classification
