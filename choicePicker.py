import sys

picks = sys.argv[1]
classes = sys.argv[2]
students = sys.argv[3]

classLimit = 3
pickLimit = 4
sneakyStudents = []

class Choice(object):
    def __init__(self, subject, classes, groupLimit):
        self.subject = subject.rstrip(",\n")
        self.classes = {}
        self.students = []
        self.sneakyStudents = []
        self.groupLimit = groupLimit
        for className in classes:
            self.classes[className] = 0

    def incrementClass(self, nameOfClass):
        self.classes[nameOfClass] += 1

    def checkSpot(self, nameOfClass):
        status = False
        if (len(self.students) < self.groupLimit):
            if (self.classes[nameOfClass] < classLimit):
                status = True
            else:
                status = False
        return status

    def addStudent(self, nameOfStudent, nameOfClass):
        self.students.append(nameOfStudent + "," + nameOfClass)
        self.classes[nameOfClass] += 1
        # print(nameOfStudent + " added to " + self.subject)


    def numberOfStudents(self):
        return len(self.students)

def createArrayFromCSV(filename):
    fileToRead = open(filename, "r").readlines()
    array = []
    for element in fileToRead:
        array.append(element.rstrip(",\n"))
    return array

def createDictFromCSV(filename, array):
    fileToRead = open(filename, "r").readlines()
    aDict = {}
    for element in fileToRead:
        arrayFromElement = element.split(",")
        nameOfChoice = arrayFromElement[0]
        groupLimit = int(arrayFromElement[1])
        aDict[nameOfChoice] = Choice(nameOfChoice, array, groupLimit)
    return aDict

def addOddStudent(nameOfStudent, nameOfClass, reason):
    sneakyStudents.append(nameOfStudent + "," + nameOfClass + "," + "ej placerad" + "," + reason)


arrayOfClasses = createArrayFromCSV(classes)
allChoices = createDictFromCSV(picks, arrayOfClasses)
arrayOfStudents = createArrayFromCSV(students)

for student in arrayOfStudents:
    studentArray = student.split(",")
    studentName = studentArray[0]
    studentClass = studentArray[1]
    studentPicks = studentArray[2:]

    if (len(studentPicks) > pickLimit):
        reason = str(len(studentPicks)) + " val"
        addOddStudent(studentName, studentClass, reason)

    else:
        count = 0
        pick = False
        for pick in studentPicks:
            if allChoices[pick].checkSpot(studentClass):
                allChoices[pick].addStudent(studentName, studentClass)
                pick = True
                break
            else:
                pass
            count += 1
        if (pick and count == 4):
            addOddStudent(studentName, studentClass, "ingen plats")


fileForPicks = open("sortedPicks.csv", "w")

for pick in allChoices:
    for student in allChoices[pick].students:
        fileForPicks.write(student + "," + allChoices[pick].subject + "\n")

for student in sneakyStudents:
    fileForPicks.write(student + "\n")
