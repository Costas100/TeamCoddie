from pymongo import MongoClient
import csv

#change from local server to Homer server
server = MongoClient("127.0.0.1")
#server = MongoClient('homer.stuy.edu')

#creating the database
db = server.teamcoddiedb

#creating the collection
c = db.students

#opening up the csv/data files
fObjP = open("peeps.csv")
p=csv.DictReader(fObjP)




print p
for i in p:
    #creates a dictionary of the peeps data: name, age, id
    dPeeps = {"name":i["name"], "age":i["age"], "id":i["id"]}
    
    fObjC = open("courses.csv")
    co = csv.DictReader(fObjC)
    
    for j in co:
       # print j
        #if id from peeps data matches with id from courses data,
        #add the mark for the specific course to the dictionary
        if j["id"] == dPeeps["id"]:
            dPeeps[j["code"]]= j["mark"]
            
    print dPeeps
    #insert the dictionary/document into the collection
    c.insert_one(dPeeps)
    #after first insertion using local, it says that target machine actively refused connection
    #after first insertion using homer, it says that the server time out

#--------------testing out insertions of dictionaries--------
'''
num = 0
c2 = db.numbers
while num < 10:
    numDict = {"number":num}
    num=num+1
    print numDict
    c2.insert_one(numDict)
    ##after the first insertion, it says that the server timed out 

'''


    
