import pymongo
from pymongo import MongoClient
import datetime

#it is a database like MySQL
#you can save data as dictionaries and then define look up table, find data, search database, etc.

#first download MongoDB community server for windows:https://www.mongodb.com/try/download/community
#second download robomongo and install it:https://robomongo.org/
 
client = MongoClient('mongodb://localhost:27017/') #connect to mongo service
client = MongoClient()
db = client.mahdi_db

Users = db.users

current_date = datetime.datetime.now()
desired_date = datetime.datetime(2009, 8, 11)


user1 = {'username': "nick", 
         'password':'zxcvbnm', 
         'favorite_num': 127, 
         'hobbies':['python','game','pizza'],
         "date": current_date}

user2 = {'username': "tom", 
         'password':'zxcvbnm', 
         'favorite_num': 127, 
         'hobbies':['python','game','pizza'],
         "date": current_date}

user3 = {'username': "ali", 
         'password':'zxcvbnm', 
         'favorite_num': 127, 
         'hobbies':['python','game','pizza'],
         "date": current_date}

user4 = {'username': "ahmad", 
         'password':'zxcvbnm', 
         'favorite_num': 127, 
         'hobbies':['python','game','pizza'],
         "date": current_date}

#inserting one by one
inserted = Users.insert_one(user1)
inserted = Users.insert_one(user2)

#inserting bulk:
inserted = Users.insert_many([user3, user4])

client.database_names() #list of databases

#now database is created so you can go and open Studio 3T (i.e. robomongo) to see inserted.
#To see databases first, by top left corner icon, define a local host, and connect to it 

#accessing inserted features
inserted.inserted_ids

#how to find a username by specific features:
Users.find({"username": 'nick', 'favorite_num': 127}).count()

#finding entities inserted before a certain date:
Users.find({"date": {"$gte": desired_date}}).count()

#check whether a specific features existis:
Users.find({"date": {"$exists": True}}).count()

#you should first give index to data:
Users.create_index([("username", pymongo.ASCENDING)], unique=True)

#deleting database:
client.drop_database('mahdi_db') 
