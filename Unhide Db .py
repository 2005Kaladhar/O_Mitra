import os
from tinydb import Query, TinyDB
try:
    db = TinyDB("SubjectAndDays.db")
    names_of_db = ["SubjectAndDays.db", 'SubjectsAndTimes.db', 'Linkdic.db', 'sublist.db', 'personaldetails.db']
    for file in names_of_db:
        os.system(f"attrib +h +s +r {file}")
    print("all the files are unhide...")

except PermissionError as e :
    names_of_db = ["SubjectAndDays.db", 'SubjectsAndTimes.db', 'Linkdic.db', 'sublist.db', 'personaldetails.db']
    for file in names_of_db:
        os.system(f"attrib -h -s -r {file}")
    print("all the files are unhide...")
    
