# PasswordGenerator

PasswordGenerator is command line tool for generating password.

## Requirements
python3

## Usage
Run command from command line.

    $ python password_generator.py
    u/`vl/UIoa

Default settings is as follows.
- Generated password contains alphabets, digits and symbols
 - Symbols are printable characters other than alphabets and digits
- The length of generated password is 10

## Examples
If you would like to set password length to 12, run following command.

    $ python password_generator.py -l 12
    F|@hH@z.ia@`

If you would like to change symbols contained in password, run following command.

    $ python password_generator.py -s '_=&'
    X&7n_HfdGZ
