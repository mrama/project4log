import sys

file = input("Input filename: ")
try:
    logs = open(file)
except:
    print("Invalid filename")
    sys.exit()

errors = {"trace": 0, "debug": 0, "info": 0, "warning": 0,
        "error": 0, "fatal": 0, "off": 0}
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
        error = input("Error " + email + " is subscribed to: ").lower()
        if error == "":
            continue
        if error in emails:
            emails[error].add(email)
        else:
            print("Invalid error")
print(emails)
