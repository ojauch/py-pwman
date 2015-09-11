#!/usr/bin/python3
# -*- coding: utf-8 -*-

from hashlib import pbkdf2_hmac
import pyperclip.pyperclip
import time
import argparse
from getpass import getpass

lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
upper_case_letters = list('ABCDEFGHJKLMNPQRTUVWXYZ')
numbers = list('0123456789')
special_characters = list('#!"§$%&/()[]{}=-_+*<>;:.')
password_characters = lower_case_letters + upper_case_letters + numbers + special_characters
salt = 'pepper'
paste_time = 12

def convert_bytes_to_password(hashed_bytes, length):
	number = int.from_bytes(hashed_bytes, byteorder='big')
	password = ""
	while number > 0 and len(password) < length:
		password = password + password_characters[number % len(password_characters)]
		number = number // len(password_characters)
	return password

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--print", help="prints generated password to command line",
					action="store_true")
parser.add_argument("-c", "--copy", help="copies generated password to clipboard (default)",
					action="store_true")
parser.add_argument("-t", "--time", help="set time the password is stored in clipboard (default=12s)", type=int)
parser.add_argument("-mp", "--master_password", help="provide master password to generate password", type=str)
parser.add_argument("-d", "--domain", help="provide domain name to generate password", type=str)
args = parser.parse_args()

if args.time:
	paste_time = args.time
	print(paste_time)

if args.master_password != "":
	master_password = args.master_password
else:
	master_password = getpass('master password: ')

if args.domain != "":
	domain = args.domain
else:
	domain = input('domain: ')
	while len(domain) < 1:
		print('Please provide a domain name.')
		domain = input('domain: ')

hash_string = domain + master_password
hash_string_bytes = hash_string.encode('utf-8')
salt = 'pepper'
salt_bytes = salt.encode('utf-8')
hashed_bytes = pbkdf2_hmac(
	'sha512',
	hash_string_bytes,
	salt_bytes,
	4096)

if args.print:
	print('password: ' + convert_bytes_to_password(hashed_bytes, 10))
else:
	pyperclip.copy(convert_bytes_to_password(hashed_bytes, 10))
	print("Paste your password")
	time.sleep(paste_time)
	pyperclip.copy("")