# Ask user: Convert from C to F or F to C?
temp_scale = int(input('Convert from (1=C to F, 2=F to C): '))
# Ask for temperature
temp_value = float(input('Temperature Value: '))

# Use if/else to do the right conversion
if temp_scale == 1:
    print(f'Temperature in F: {(9/5)*temp_value + 32}')
else:
    print(f'Temperature in C: {(5/9)*(temp_value - 32)}')

# Print result
