import dbm
import random

ROSTER = (
    "Krishna",
    "Emely",
    "Demi",
    "Gregory",
    "Spencer",
    "Myat",
    "Carmen",
    "Victoria",
    "Jinna",
    "Nico",
    "Meiling",
    "Jenny",
    "Shaun",
    "Brian",
    "David",
    "Patrick",
    "Shirley",
    "Arteen",
    "Julie",
)

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-"]

db = dbm.open("Classwork/Session 14/db_student.db", "c")

for student in ROSTER:
    db[student] = random.choice(GRADES)

for key in db:
    print(key, db[key])


db.close()