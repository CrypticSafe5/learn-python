def print_average():
    keepLooping = True
    listOfNumbers = []
    while keepLooping == True:
        value = int(input("Input value: "))
        if value < 0:
            keepLooping = False
            if len(listOfNumbers) == 0:
                print("Divide by 0 error!")
            else:
                print("Output:", sum(listOfNumbers)/len(listOfNumbers))
        else:
            listOfNumbers.append(value)
print_average()
