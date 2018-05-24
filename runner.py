import sys
import analysis

file = input("Input filename: ")
try:
    logs = open(file)
except:
    print("Invalid filename")
    sys.exit()

errors = {"TRACE": 0, "DEBUG": 0, "INFO": 0, "WARNING": 0,
        "ERROR": 0, "FATAL": 0, "OFF": 0}
emails = {}
for error in errors:
    emails[error] = set()

print("Input email address followed by all errors subscribed to")
print("Blank email address stops email address input, blank error stops error"
" input")
email = " "
while email != "":
    email = input("Email address: ").lower()
    if email == "":
        continue
    error = " "
    while error != "":
        error = input("Error " + email + " is subscribed to: ").upper()
        if error == "":
            continue
        if error in emails:
            emails[error].add(email)
        else:
            print("Invalid error")

analysis.parse(logs, errors, emails)
print("dict from parse: ", errors)
