from string import ascii_letters, digits, punctuation
from secrets import choice
from passlib.hash import bcrypt
from zxcvbn import zxcvbn
class Password:
    """Generates password
    and verify if password is secure"""
    @classmethod
    def gen_password(cls):
        characters_pass = ascii_letters + digits + punctuation
        password = str(''.join(choice(characters_pass) for _ in range(12)))
        pass_security = zxcvbn(password)

        while pass_security['score'] < 3:
            password = cls.gen_password()

        return password
    @classmethod
    def encrypt_password(cls, password: str):
        return bcrypt.hash(password)
    @classmethod
    def verify_password(cls, password: str, hashed_password: str):
        return bcrypt.verify(password, hashed_password)





if __name__ == '__main__':

    print(Password.encrypt_password(Password.gen_password()))

    password_generator =  Password.gen_password()
    encrypt_pass = Password.encrypt_password(password_generator)
    print(encrypt_pass)