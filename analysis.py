from operator import itemgetter
import re

def parse_timestamp(timestamps, line):
    timestamp_pattern = re.compile("(\d*):(\d*):(\d*)")
    timestamp = timestamp_pattern.search(line)
    if timestamp:
        hour = timestamp.group(1)
        if hour:
            hour = int(hour)
            if "GMT+05" in timestamp.string:
                hour -= 9
            if not hour in timestamps:
                timestamps[hour] = 0
            timestamps[hour] += 1

def parse(f, errors, emails, num_emails, timestamps):
    context = ["" for i in range(5)]
    lines = []
    for line in f:
        lines.append(line)
    for i in range(len(lines)):
        line = lines[i]
        for j in range(-2,3):
            line_index = i+j
            context_index = j+2
            if line_index >= 0 and line_index < len(lines):
                context[context_index] = lines[line_index]
            else:
                context[context_index] = ""
            if context_index == 2:
                context[context_index] = "Current Error >>> " + context[context_index]
            else:
                context[context_index] = "                  " + context[context_index]
        if "[CM" in line or line[0] == "<":
            parse_timestamp(timestamps, line)
        elif "[CM" in context[1] or context[1][0] == "<":
            parse_timestamp(timestamps, line)
        for word in line.split():
            if (word.startswith("<")):
                word = word.upper()
            for key in errors:
                if (key in word):
                    errors[key] += 1
                    for email in emails[key]:
                        num_emails[email] += 1
                        print("Email to " + email + " about " + key + ":")
                        for i in range(5):
                            if context[i] != "":
                                print(context[i])

def num_errors(errors):
    count = 0
    for error in errors:
        if errors[error] > 0:
            count += 1
    return count

def most_to_least(data):
    list = []
    for elem in data:
        if data[elem] > 0:
            list.append((elem, data[elem]))
    list = sorted(list, key=itemgetter(1))
    res = []
    for elem in list:
        res.insert(0, elem)
    return res

