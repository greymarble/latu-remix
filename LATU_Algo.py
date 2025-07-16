from LATU_Obj import *
from LATU_Const import *

def create_student_obj(student: str) -> Person:
    """
    Create a person object of the student <student>. The Salmon data is included in 
    a <student>pref.csv file under the directory studentData. 


    csv file has 45 lines
    """
    with open(f'studentData/{student}pref.csv', 'r') as file:
        person = Person(file.readline().strip().split(',')[1])

        currLine = file.readline().strip()
        lineNum = 1

        locationIndex = 0
        dateIndex = 0

        while currLine:
            currLine = currLine.rsplit(',', maxsplit=1)

            prefMap = Option(currLine[0], currLine[1])
            person.prefs[locationIndex].dates[dateIndex].add(prefMap)
            # print(list(person.prefs[locationIndex].dates[dateIndex]))

            if lineNum % 3 == 0:
                dateIndex = (dateIndex + 1) % 3
            if lineNum % 9 == 0:
                locationIndex += 1

            lineNum += 1
            currLine = file.readline().strip()

        
        return person
    
def create_all_students() -> set[Person]:
    """
    """
    ...


def main():
    create_student_obj('kaito')

if __name__ == '__main__':
    main()