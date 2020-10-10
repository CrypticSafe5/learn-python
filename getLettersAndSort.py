import requests

"""
Pull back text and get the counts of the letters and sort them from most used to least used
http://jefflutgen.com/cosc120/alice.txt
"""
def countLetters():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letterCounterDict = {}
    response = requests.get("http://jefflutgen.com/cosc120/alice.txt")
    rawLetters = response.text.lower()
    for i in rawLetters:
        if i in alphabet:
            if i in letterCounterDict:
                letterCounterDict[i] += 1
            else:
                letterCounterDict[i] = 1
    sortedDict = sorted(letterCounterDict.items(), key=lambda x: x[1], reverse=True)
    for i in sortedDict:
        print(i[0], i[1])
countLetters()
