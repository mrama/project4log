def parse(f, errors, emails):
    for word in f.read().split():
        if (word.startswith("<")):
            word = word.upper()
        for key in errors:
            if (key in word):
                errors[key] = errors.get(key, 0) + 1    
                for email in emails[key]:
                    print("Send email to " + email + " about " + key)

