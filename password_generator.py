#-*- coding:utf8 -*-
from optparse import OptionParser, OptionValueError
import random

PASSWORD_MIN_LENGTH = 3
DEFAULT_SYMBOLS = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def generate_password(length=10, symbol=""):
    """
    Generate password.

    Args:
        length(int): Password length. It must be greater than PASSWORD_MIN_LENGTH - 1.
        symbol(str): Symbols contained in password.
    
    Returns:
        str: Generated password.
    """

    if length < PASSWORD_MIN_LENGTH:
        raise ValueError("length must be greater than %d." % (PASSWORD_MIN_LENGTH - 1))

    letters = [chr(c + ord('a')) for c in range(26)]
    captials = [chr(c + ord('A')) for c in range(26)]
    digits = [chr(c + ord('0')) for c in range(10)]
    alnum = letters + captials + digits

    password_chars = alnum
    if symbol:
        password_chars += [c for c in symbol if (not c in alnum)]

    # select at least one character from uppercase letter, lowercase letter, and symbol
    password = []
    password += random.choice(letters)
    password += random.choice(captials)
    password += random.choice(digits)
    if symbol:
        password += random.choice(symbol)

    # generate password
    for i in range(length - len(password)):
        password += random.choice(password_chars)
    
    # shuffle password because its head is 
    random.shuffle(password)
    return "".join(password)

if __name__ == '__main__':
    def check_length(option, opt_str, value, parser):
        if value < PASSWORD_MIN_LENGTH:
            raise OptionValueError("Password length must be greater than %d." % (PASSWORD_MIN_LENGTH - 1))
        setattr(parser.values, option.dest, value)

    # parse command line options
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-l", "--length", action="callback", type="int", default=10, help="length of password", metavar="Password Length", callback=check_length)
    parser.add_option("-s", "--symbol", type="string", default=DEFAULT_SYMBOLS, help="symbols contained in password", metavar="Symbol Characters")
    (options, args) = parser.parse_args()

    print(generate_password(options.length, options.symbol))