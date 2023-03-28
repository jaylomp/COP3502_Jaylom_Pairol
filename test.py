
memory = 0

def encode(password):
    global memory
    encoded_password = ''
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    memory = int(encoded_password)


def decode(password):
    pass


if __name__ == '__main__':
    while True:
        print()
        print('Menu \n------------- \n1. Encode \n2. Decode \n3.Quit')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            pass
            print(f'The encoded password is {encode(password)}, and the original password is')
        elif option == 3:
            break

