groupLimit = 3

class Choice(object):
    def __init__(self, subject, classes):
        self.subject = subject.rstrip(",\n")
        self.classes = {}
        self.students = []
        for className in classes:
            self.classes[className] = 0

    def incrementClass(self, nameOfClass):
        self.classes[nameOfClass] += 1

    def checkSpot(self, nameOfClass):
        status = False
        if (len(self.students) < 15):
            if (self.classes[nameOfClass] < groupLimit):
                status = True
            else:
                status = False
        return status

    def addStudent(self, nameOfStudent, nameOfClass):
        self.students.append(nameOfStudent + "," + nameOfClass)
        self.classes[nameOfClass] += 1
        print(nameOfStudent + " added to " + self.subject)


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
        aDict[element.rstrip(",\n")] = Choice(element, array)
    return aDict


arrayOfClasses = createArrayFromCSV("classes.csv")
allChoices = createDictFromCSV("picks.csv", arrayOfClasses)
arrayOfStudents = createArrayFromCSV("students.csv")
    
for student in arrayOfStudents:
    studentArray = student.split(",")
    studentName = studentArray[0]
    studentClass = studentArray[1]
    studentPicks = studentArray[-4:]
    for pick in studentPicks:
        print(allChoices[pick].classes)
        if allChoices[pick].checkSpot(studentClass):
            allChoices[pick].addStudent(studentName, studentClass)
            break
        else:
            pass
        
fileForPicks = open("sortedPicks.csv", "w")

for pick in allChoices:
    for student in allChoices[pick].students:
        fileForPicks.write(student + "," + allChoices[pick].subject + "\n")
