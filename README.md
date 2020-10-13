# Password Analyser
Check to see if a password is safe using many different methods, including HavIBeenPwned and comparing it to a list of over 100000+ common passwords.
No sensitive information is shared at all. Only the first five characters of the SHA-1 hash is uploaded to HaveIBeenPwned, all others processes are competed locally on the computer.

# Requirements
`pip install requests termcolor colorama hashlib argparse`

# Installation
If you haven't already, install git [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Then, clone the repository to your local machine with:
`git clone https://github.com/KilianPlapp/password-analyser.git`  

# Usage
Change directories into the cloned repository.
`cd password-analyser`

To run:
`python3 password-analyser.py PASSSWORD`   
Replace PASSWORD with your desired password  
Or, to read a password from a file:  
`python3 password-analyser.py -f FILE`   
