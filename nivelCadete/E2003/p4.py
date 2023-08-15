def extract_digits(number):
    # Convert the number to a string
    num_str = str(number)
    # Extract and return the digits as a list of integers
    digits = [int(digit) for digit in num_str]
    return len(digits)

# Example usage
'''
given_number = 10
digits = extract_digits(given_number)
print("Digits of the number:", digits)
'''
sum=0
i=1   
while True:
    sum = sum + extract_digits(i)
    if sum >= 35:
        break
    i += 1
    
print(i)
