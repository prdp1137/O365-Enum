import requests
import re
import argparse

requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro)', 'Accept': 'application/json'}

argparser = argparse.ArgumentParser(description='Check if an email exists on Office365')
argparser.add_argument('-f', '--file', help='File containing emails', required=True)
args = argparser.parse_args()

if args.file:
	emailsFile = args.file
else:
	print("[-] No file specified. Program will exit.")
	exit()

try:
	with open(emailsFile, 'r') as f:
		emails = f.readlines()
except:
	print("[-] File not found. Program will exit.")
	exit()

for email in emails:
	emailToVerify = email.replace('\n', '')
	if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", emailToVerify):
		print("{} is not a valid email.".format(emailToVerify))
		continue

	url = 'https://outlook.office365.com/autodiscover/autodiscover.json/v1.0/{}?Protocol=Autodiscoverv1'.format(emailToVerify)

	try:
		r = requests.get(url, verify=False, headers=headers, allow_redirects=False, timeout=1)
	except requests.exceptions.Timeout:
		print("{} does not exist.".format(emailToVerify))
		continue
	
	print("{} exists.".format(emailToVerify))
