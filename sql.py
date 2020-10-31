import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="practice"
)

def removeStudent():
    _name = getName()
    sql = "DELETE FROM student WHERE name = '{}'".format(_name)
    mycursor.execute(sql)
    mydb.commit()

def addId():
    mycursor.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

def display():
    mycursor.execute("SELECT * FROM student")
    print(mycursor.fetchall())

def getName():
    name = str(input("Enter a name: "))
    return name

def getGrade():
    grade = str(input("Enter their grade: "))
    while grade != "Freshman" and grade != "Sophmore" and grade != "Junior" and grade != "Senior":
        grade = str(input("You must enter Freshman, Sophmore, Junior or Senior: "))
    return grade

def getAge():
    age = int(input("Enter age: "))
    while age < 14 or age > 19:
        age = int(input("Enter a valid age: "))
    return age

def getGpa():
    gpa = float(input("Enter a gpa: "))
    while gpa < 0.0 or gpa > 4.0:
        gpa = float(input("Enter a valid gpa: "))
    return gpa

def getSex():
    sex = str(input("Enter their sex(M/F): "))
    while sex != "F" and sex != "M":
        sex = str(input("Enter their sex(M/F): "))
    return sex

def printInstructions():
    print("Enter Q to quit")
    print("Enter A to add")
    print("Enter D to display the table")
    print("Enter I to display instructions")
    print("Enter R to remove a student")

def addStudent():
    name = getName()
    grade = getGrade()
    age = getAge()
    gpa = getGpa()
    sex = getSex()
    sql = "INSERT INTO student (name, grade, age, gpa, sex) VALUES (%s, %s, %s, %s, %s)" 
    val = (name, grade, age, gpa, sex)
    mycursor.execute(sql, val)
    mydb.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM student")
print(mycursor.fetchall())

a = 'a'
printInstructions()
while a != 'Q':
    a = str(input("Choose an option: "))
    if a == 'A':
        addStudent()
    elif a == 'Q':
        break
    elif a == 'D':
        display()
    elif a == 'I':
        printInstructions()
    elif a == 'R':
        removeStudent()
    else:
        print("Not a valid option!")

print("Adding student Id to the table")
addId()
display()


mycursor.execute("ALTER TABLE student DROP COLUMN id")