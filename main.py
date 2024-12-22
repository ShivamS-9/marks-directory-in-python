import csv
from prettytable import PrettyTable

# First Name, Last Name, Roll Number, Course Name, Semester, Exam Type, Total Marks and Scored Marks


def Entry():
    first = input("Enter first name: ")
    last = input("Ente last name: ")
    roll = input("Enter roll num: ")
    course = input("Enter course name: ")
    sem = input("Enter sem: ")
    exam = input("Enter exam type: ")
    total = input("Total marks: ")
    scored = input("Marks scored: ")
    return [first, last, roll, course, sem, exam, total, scored]


class MarksDirectory:
    heading = [
        "First Name",
        "Last Name",
        "Roll Number",
        "Course Name",
        "Semester",
        "Exam Type",
        "Total Marks",
        "Scored Marks",
    ]

    def __init__(self):
        self.dir = []

    def add(self, entryList):
        self.dir.append(entryList)
        print("Roll number {} added.".format(entryList[2]))

    def loadFromCsv(self, myFile):
        with open(myFile, "r") as myFileR:
            head = csv.DictReader(myFileR)

            for row in head:
                self.dir.append(
                    {
                        "First Name": row["First Name"],
                        "Last Name": row["Last Name"],
                        "Roll Number": int(row["Roll Number"]),
                        "Course Name": row["Course Name"],
                        "Semester": row["Semester"],
                        "Exam Type": row["Exam Type"],
                        "Total Marks": int(row["Total Marks"]),
                        "Scored Marks": int(row["Scored Marks"]),
                    }
                )
        for entry in self.dir:
            print(entry)

    def display(self):
        if not self.dir:
            print("No data.")
        else:
            table = PrettyTable()

            table.field_names = self.heading
            for entry in self.dir:
                table.add_row(entry)

            print(table)

    def remove(self, roll, rem, what):
        entries_to_remove = []

        for entry in self.dir:
            if entry[2] == roll:
                if rem == "None" and what == "None":
                    entries_to_remove.append(entry)
                elif rem != "None" and what != "None":
                    if entry[what] == rem:
                        entries_to_remove.append(entry)

        for entry in entries_to_remove:
            self.dir.remove(entry)
            print("Entry removed.")

        if not entries_to_remove:
            print("No matching entry found.")

    def update(self, roll, fieldUpdating, newField):
        for entry in self.dir:
            if entry[2] == roll:
                entry[self.heading.index(fieldUpdating)] = newField
                print("Updated.")
                break
        else:
            print("Roll number not found.")

    def search(self, searchVal, searchCol):
        searchVal = searchVal.lower()
        printList = []
        heading = [
            "First Name",
            "Last Name",
            "Roll Number",
            "Course Name",
            "Semester",
            "Exam Type",
            "Total Marks",
            "Scored Marks",
        ]
        for entry in self.dir:
            flag = False

            for col in searchCol:
                val = str(entry[heading.index(col)]).lower()
                if searchVal in val:
                    flag = True
                    break

            if flag == 1:
                printList.append(entry)

        if not printList:
            print("No matching entry")
        else:
            print("Matching entries")
            for entry in printList:
                print(entry)


marks_dir = MarksDirectory()
while True:
    print("Please choose one of the options.")
    print(
        " For adding new entry: 1 \n For loading into CSV: 2 \n For displaying whole database: 3 \n For removing entries: 4 \n For updation: 5 \n For searching: 6\n For exiting the program: 0"
    )

    val = input()

    match val:
        case "1":  # add
            entryList = []
            entryList = Entry()
            marks_dir.add(entryList)
        case "2":  # load
            myFile = input("Enter csv file name(The file should be in same folder): ")
            myFile = myFile + ".csv"
            marks_dir.loadFromCsv(myFile)
        case "3":  # display
            marks_dir.display()
        case "4":  # remove
            roll = input("Enter roll number to be removed:")
            flag = input(
                "Any specifications for removing(Course name, semester or exam type) (Y/N): "
            )
            rem = "None"
            what = "None"
            if flag == "Y" or flag == "y":
                what = input(
                    "Press C/c for course, S/s for semester, E/e for exam type "
                )
                if what == "c" or what == "C":
                    rem = input("Enter course name:")
                    what = "course"
                elif what == "s" or what == "S":
                    rem = input("Enter sem num:")
                    what = "semester"
                elif what == "e" or what == "E":
                    rem = input("Enter exam type:")
                    what = "Exam"
                marks_dir.remove(roll, rem, what)
            else:
                marks_dir.remove(roll, rem, what)

        case "5":  # update
            roll = input("Enter Roll Number to be updated: ")
            fieldUpdating = input("Enter the field to update (e.g., Total Marks): ")
            newField = input("Enter the new value: ")
            marks_dir.update(roll, fieldUpdating, newField)
        case "6":  # search
            print(
                "Welcome to search function. To search with first name enter 'first', with last name enter 'last', with roll number enter 'roll', with course enter 'course', with semester enter 'sem'. \n Enter:"
            )
            searchBy = input()
            searchBy = searchBy.lower()
            searchCol = [
                "First Name",
                "Last Name",
                "Roll Number",
                "Course Name",
                "Semester",
            ]
            match searchBy:
                case "first":
                    print("Enter first name: ")
                    f = input()
                    marks_dir.search(f, searchCol)
                case "last":
                    print("Enter last name: ")
                    l = input()
                    marks_dir.search(l, searchCol)
                case "roll":
                    print("Enter roll number: ")
                    r = input()
                    marks_dir.search(r, searchCol)
                case "course":
                    print("Enter course name: ")
                    c = input()
                    marks_dir.search(c, searchCol)
                case "sem":
                    print("Enter sem number: ")
                    s = input()
                    marks_dir.search(s, searchCol)
                case _:
                    print("Invalid input.")
        case "0":
            pass
