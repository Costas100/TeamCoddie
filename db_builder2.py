from pymongo import MongoClient
import csv

#change from local server to Homer server
#server = MongoClient("127.0.0.1")
#server = MongoClient('homer.stuy.edu')
server = MongoClient("149.89.150.100")

#creating the database
db = server.teamcoddiedb

#creating the collection
studentCollection = db.students

#opening up the csv/data files
fObjP = open("peeps.csv")
people=csv.DictReader(fObjP)





for i in people:
    #creates a dictionary of the peeps data: name, age, id
    dPeeps = {"name":i["name"], "age":i["age"], "id":i["id"]}

    fObjC = open("courses.csv")
    courses = csv.DictReader(fObjC)

    
    for j in courses:
        #if id from peeps data matches with id from courses data,
        #add the mark for the specific course to the dictionary
        if j["id"] == dPeeps["id"]:
            dPeeps[j["code"]]= j["mark"]
            
#    print dPeeps
    #insert the dictionary/document into the collection
    studentCollection.insert_one(dPeeps)


def averageMark(name):
    currentStudent= server.db.studentCollection.find({"name":name})
    print currentStudent
   # softdev, systems, greatbooks, ceramics
    for i in currentStudent:
        print i
        print
        print

#def displayAverage():
    

averageMark("kruder")
    
