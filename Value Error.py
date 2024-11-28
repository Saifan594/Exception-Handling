print('\033c')

try:
    num = int(input('Enter your number : '))
    print(num)

except ValueError as ex:
    print(f'Exception: {ex}')

print('I am outside the try block')