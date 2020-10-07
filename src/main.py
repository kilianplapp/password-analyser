# Author: https://github.com/KilianPlapp
import requests, termcolor, sys, colorama, hashlib, argparse, string

def password_analyser(userinput):
    symbol_characters = tuple(string.punctuation)
    colorama.init()
    common_passwords = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt")
    
    if(common_passwords.status_code == 200): termcolor.cprint('Succesfully Imported Common Password List!', 'green')
    else:
        termcolor.cprint(f'Error Requesting Common Password List! Code: {common_passwords.status_code}', 'red')
        sys.exit()
    
    y = hashlib.sha1(userinput.encode())
    sha_1 = y.hexdigest()
    haveibeenpwnedapi = requests.get(f"https://api.pwnedpasswords.com/range/{sha_1[:5]}")

    if(haveibeenpwnedapi.status_code == 200): termcolor.cprint('Succesfully Contacted HaveIBeenPwned API!', 'green')
    else:
        termcolor.cprint(f'Error Contacting HaveIBeenPwned API! Code: {haveibeenpwnedapi.status_code}', 'red')
        sys.exit()
    
    for line in haveibeenpwnedapi.text.splitlines():
        z = line.split(':')
        if(z[0].lower() == sha_1[5:]):
            pwned = True
            break
    else: pwned = False

    for line in common_passwords.text.splitlines():
        if(line == userinput):
            is_a_common_password = True
            break
    else: is_a_common_password = False

    if(len(userinput) >= 8): over_eight_characters = True
    else: over_eight_characters = False

    for letter in userinput:
        if(letter.isupper()):
            contains_upper_case = True
            break
    else: contains_upper_case = False

    for letter in userinput:
        if(letter in symbol_characters):
            symbol_used = True
            break
    else: symbol_used = False
    
    print("---------------------------------------")
    if(is_a_common_password): termcolor.cprint('Is a common password!', 'red')
    else: termcolor.cprint('Is not a common password!', 'green')
    if(over_eight_characters): termcolor.cprint('Contains eight or more characters!', 'green')
    else: termcolor.cprint('Below eight characters!', 'red')
    if(contains_upper_case): termcolor.cprint('Contains atleast one uppercase character!', 'green')
    else: termcolor.cprint('Does not contain at least one uppercase character!', 'red')
    if(symbol_used): termcolor.cprint('Contains a symbol!', 'green')
    else: termcolor.cprint('Does not contain a symbol!', 'red')
    if(pwned): termcolor.cprint(f'Password Pwned {z[1]} times! ','red')
    else: termcolor.cprint("Password not Pwned!", 'green')
    print("---------------------------------------")
