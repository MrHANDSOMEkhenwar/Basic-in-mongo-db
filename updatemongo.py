from pymongo import MongoClient
ct=MongoClient('localhost',27017)
db=ct['mongodb']
cm=db['staff']
cond={'empid':101}
newv={'$set':{'salary':78000}}
cm.update_one(cond,newv)
print('Updated')
