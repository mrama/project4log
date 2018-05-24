#import init
errorDict = {"trace": 0, "debug": 0, "info": 0, "warning": 0,
        "error": 0, "fatal": 0, "off": 0}

f = open("test.txt")

def parse(text):
    for word in f.read().lower().split():
        if (word in errorDict):
            errorDict[word] = errorDict.get(word, 0) + 1

    print("updated dict: ", errorDict)
    return errorDict

parse(f)
