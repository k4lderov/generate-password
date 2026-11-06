import secrets
import string

DIGITS    = list(string.digits)
LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
SYMBOLS   = ['!', '@', '#', '$', '%', '&', '*', '_', '-', '+']

ALL_CHARACTERS = DIGITS + LOWERCASE + UPPERCASE + SYMBOLS

MAX_LENGTH = 20
MIN_LENGTH = 16

def generate_password(password_length):
    if not MIN_LENGTH <= password_length <= MAX_LENGTH:
        raise ValueError

    password = [
        secrets.choice(DIGITS),
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(SYMBOLS)
    ]

    while len(password) < password_length:
        password.append(secrets.choice(ALL_CHARACTERS))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    try:
        user_input = input(f'Password length ({MIN_LENGTH}-{MAX_LENGTH}): ').strip()

        if not user_input:
            raise ValueError

        password_length = int(user_input)
        password = generate_password(password_length)
        
        print(f'Password: {password}')
    except ValueError:
        print(f'An error has occurred...')
