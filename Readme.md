# O365 Enum
This is a simple python script which can be used to enumerate if the email address within the Office 365 exists or not. This is totally dependable upon autodiscover protocol and the logic that if the email does not exist, the response from the server is timed-out this giving no result. If the email exists, response is obtained immediately.

## Requirements:
- argparse for parsing arguments
- re for regex
- requests for sending HTTP request to outlook.office365.com

## Installation
```
git clone https://github.com/pr0d33p/O365-Enum
```

## Usage
```
python3 main.py -f emails.txt # assuming that the emails to enumerate are stored within the emails.txt file.
```
