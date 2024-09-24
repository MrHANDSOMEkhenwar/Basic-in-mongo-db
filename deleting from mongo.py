from pymongo import MongoClient
ct=MongoClient('localhost',27017)
db=ct['mongodb']
cm=db['staff']
xa=int(input('Enter your EMPID :'))
qt={'empno':xa}

cm.delete_one(qt)
print('DATA deleted')
