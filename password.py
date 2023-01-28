from string import ascii_letters, digits, punctuation
from secrets import choice
from passlib.hash import bcrypt
from zxcvbn import zxcvbn
def gen_password():
    characters_pass = ascii_letters + digits + punctuation
    return str(''.join(choice(characters_pass) for _ in range(12)))

def encrypt_password(password: str):
    return bcrypt.hash(password)

def pass_secure(password: str):
    result = zxcvbn(password)
    return result

def verify_password(password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)

if __name__ == '__main__':
    print(gen_password())
    print(encrypt_password(gen_password()))
    print(pass_secure(gen_password()))