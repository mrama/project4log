#import init
errorDict = {"TRACE": 0, "DEBUG": 0, "INFO": 0, "WARNING": 0,
        "ERROR": 0, "FATAL": 0, "OFF": 0}

f = open("scrubbed_logs.txt")

def parse(text):
    for word in f.read().split():
        if (word.startswith("<")):
            word = word.upper()
        for key in errorDict:
            if (key in word):
                errorDict[key] = errorDict.get(key, 0) + 1    
    print("updated dict: ", errorDict)
    return errorDict

parse(f)
