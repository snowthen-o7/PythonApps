#! python3
#! phoneAndEmail.py - Finds phone numbers and email addresses in the clipboard
"""
Get text off clipboard
Find all phone numbers + emails
Paste them into clipboard
Use 'pyperclip' module to copy/paste strings
Create 2 regex for phone numbers and emails
find all matches of both regexes
format matches into 1 string
display message if no matches found
"""

import pyperclip, re

# Phone Regex - Can be expanded
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code
	([^\S\n]|-|\.)?					# separator
	(\d{3})						# first 3 digits
	([^\S\n]|-|\.)					# separator
	(\d{4})						# last 4 digits
	([^\S\n]*(ext|x|ext.)[^\S\n]*(\d{2,5}))?	# extension
)''', re.VERBOSE)

# Email Regex - Can be expanded
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+				# username
	@						# @ symbol
	[a-zA-Z0-9.-]+					# domain name
	(\.[a-zA-Z]{2,4})				# TLD (Top-Level Domain)
)''', re.VERBOSE)

# TODO: URL, date regex

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
