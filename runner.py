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

num_emails = {}
for error in emails:
    for email in emails[error]:
        num_emails[email] = 0
timestamps = {}
analysis.parse(logs, errors, emails, num_emails, timestamps)
num_errors = analysis.num_errors(errors)
worst_to_best = analysis.most_to_least(errors)
frequent_to_unfrequent = analysis.most_to_least(timestamps)
if num_emails != {}:
    print("Email Summary:")
for email in num_emails:
    print(email + ": " + str(num_emails[email]) + " emails sent")
print("There are " + str(num_errors) + " unique errors in the log.")
print("From most to least problematic, the different error categories are:")
for error in worst_to_best:
    print(error[0] + ": " + str(error[1]) + " times")
print("From most to least common, the hours of the day when errors occured are:")
for hour in frequent_to_unfrequent:
    print(str(hour[0]) + ": " + str(hour[1]) + " times")
