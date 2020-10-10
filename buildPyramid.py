"""
////////////////\\\\\\\\\\\\\\\\
////////////********\\\\\\\\\\\\
////////****************\\\\\\\\
////************************\\\\
********************************

Dashes: 32, 24, 16, 8, 0
Stars:  0, 8, 16, 24, 32
"""

def buildPyramid(height):
    width = (height * 8) - 8
    for lineNumber in range(0, height):
        stars = lineNumber * 8
        dashes = int((width - stars) / 2) # Converted to int because the division converts to float and you can't multiply string by float
        print("/"*dashes + "*"*stars + "\\"*dashes)

userInput = int(input("Height of pyramid: "))
buildPyramid(userInput)
