import sys

currentPick = sys.argv[1]
allPicks = sys.argv[2]

def createArrayFromCSV(filename):
    fileToRead = open(filename, "r").readlines()
    array = []
    for element in fileToRead:
        array.append(element.rstrip(",\n"))
    return array

def createChoiceDict(filename):
    fileToRead = open(filename, "r").readlines()
    aDict = {}
    for element in fileToRead:
        arrayFromElement = element.split(",")
        studentName = arrayFromElement[0]
        currentPick = arrayFromElement[2]
        aDict[studentName] = currentPick.rstrip()
    return aDict

studentsAndAllPicks = createArrayFromCSV(allPicks)
picksDict = createChoiceDict(currentPick)
fileForPicks = open("filteredPicks.csv", "w")
fileForPicks.write("namn, klass, val \n")

for student in studentsAndAllPicks:
    arrayFromElement = student.split(",")
    studentName = arrayFromElement[0]
    for pick in arrayFromElement[2:]:
        if (pick == picksDict[studentName]):
            arrayFromElement.remove(pick)
            fileForPicks.write(",".join(arrayFromElement) + "\n")


