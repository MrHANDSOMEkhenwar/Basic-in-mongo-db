from pymongo import MongoClient
ct=MongoClient('localhost',27017)
db=ct['mongodb']
cm=db['staff']
xa=int(input('Enter your EMPID :'))
xb=input('Enter your Name :')
xd=input('Enter your City :')
xe=int(input('Enter your Salary :'))
data={'empno':xa,'name':xb,'city':xd,'salary':xe}
cm.insert_one(data)
print('DATA SAVED')
