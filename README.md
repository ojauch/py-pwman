# Python Password Manager
This is a modified command line Python version of the c't password manager.

The tool generates from a master password and a domain name a unique password for each service.

## Installation
To install py-pwman you have to install the python packet manager pip3 and the package setuptools first. Then you can install py-pwman with `sudo pip3 install [PATH_TO_SRC_DIR]`
To use the tool on Ubuntu you have to install xclip with `sudo apt-get install xclip`.

## Usage
pwman [-h] [-p] [-c] [-t TIME] [-mp MASTER_PASSWORD] [-d DOMAIN]
[-i ITERATIONS] [-s SALT] [-l LENGTH]

optional arguments:
  -h, --help            show help message and exit

  -p, --print           prints generated password to command line

  -c, --copy            copies generated password to clipboard (default)

  -t TIME, --time TIME  set time the password is stored in clipboard (default=12s)

  -mp MASTER_PASSWORD, --master_password MASTER_PASSWORD provide master password to generate password

  -d DOMAIN, --domain DOMAIN provide domain name to generate password

  -i ITERATIONS, --iterations ITERATIONS
                        set how many times the hash algorithm iterates over
                        the password string

  -s SALT, --salt SALT  set salt

  -l LENGTH, --length LENGTH
                        set password length
