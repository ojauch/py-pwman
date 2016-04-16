#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""pwman.pwman: provides entry point main()."""

__version__ = "0.1"

from hashlib import pbkdf2_hmac
import pyperclip
import time
import argparse
from getpass import getpass

def convert_bytes_to_password(hashed_bytes, length):
	lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
	upper_case_letters = list('ABCDEFGHJKLMNPQRTUVWXYZ')
	numbers = list('0123456789')
	special_characters = list('#!"§$%&/()[]{}=-_+*<>;:.')
	password_characters = lower_case_letters + upper_case_letters + numbers + special_characters

	number = int.from_bytes(hashed_bytes, byteorder='big')
	password = ""
	while number > 0 and len(password) < length:
		password = password + password_characters[number % len(password_characters)]
		number = number // len(password_characters)
	return password

def main():
	salt = 'pepper'
	paste_time = 12
	iterations = 4096
	pw_length = 10

	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--print", help="prints generated password to command line",
						action="store_true")
	parser.add_argument("-c", "--copy", help="copies generated password to clipboard (default)",
						action="store_true")
	parser.add_argument("-t", "--time",
						help="set time the password is stored in clipboard (default=12s)",
						type=int)
	parser.add_argument("-mp", "--master_password",
						help="provide master password to generate password",
						type=str)
	parser.add_argument("-d", "--domain",
						help="provide domain name to generate password",
						type=str)
	parser.add_argument("-i", "--iterations",
						help="set how many times the hash algorithm iterates over the password string",
						type=int)
	parser.add_argument("-s", "--salt",
						help="set salt",
						type=str)
	parser.add_argument("-l", "--length",
						help="set password length",
						type=int)
	args = parser.parse_args()

	if args.time:
		paste_time = args.time
		print(paste_time)

	if args.master_password:
		master_password = args.master_password
	else:
		master_password = getpass('master password: ')

	if args.domain:
		domain = args.domain
	else:
		domain = input('domain: ')
		while len(domain) < 1:
			print('Please provide a domain name.')
			domain = input('domain: ')

	if args.iterations:
		iterations = args.iterations

	if args.length:
		pw_length = args.length

	hash_string = domain + master_password
	hash_string_bytes = hash_string.encode('utf-8')
	salt = 'pepper'
	salt_bytes = salt.encode('utf-8')
	hashed_bytes = pbkdf2_hmac(
		'sha512',
		hash_string_bytes,
		salt_bytes,
		iterations)

	if args.print:
		print('password: ' + convert_bytes_to_password(hashed_bytes, pw_length))
	else:
		pyperclip.copy(convert_bytes_to_password(hashed_bytes, pw_length))
		print("Paste your password")
		time.sleep(paste_time)
		pyperclip.copy("")
