from flask import Flask, escape, request
#import sqlite3



app = Flask(__name__)
studic={}
classdic={}
patchdic={}
stu_id=12346
class_id=549
@app.route('/')




@app.route('/students',methods=['POST'])
def create_student():
     name = request.get_json()['name']
     global stu_id
     stu_id = stu_id + 1
     studic.update({stu_id: name})   

     return{
         "id":stu_id,
         "name":name

     }

 

@app.route('/classes',methods=['POST'])
def create_class():
     name = request.get_json()['name']
     global class_id
     class_id = class_id + 1
     classdic.update({class_id: name})   
     patchdic[class_id] = {}

     return{
         "id":class_id,
         "name":name

     }



@app.route('/classes/<get_cid>',methods=['GET'])
def get_class(get_cid):
    classname=classdic.get(int(get_cid))
    return{"id":get_cid,"name":classname}
    

@app.route('/students/<get_sid>',methods=['GET'])
def get_student(get_sid):
    stdname=studic.get(int(get_sid))
    return{"id":get_sid,"name":stdname}


@app.route('/classes/<add_cid>',methods=['PATCH'])
def addnew(add_cid):
    stu_id = int(request.get_json()['stu_id'])
    add_cid = int(add_cid)
    studname=studic.get(stu_id)
    classname=classdic.get(add_cid)
    patchdic[add_cid].update({stu_id:studname})
    return{"classid":add_cid,"classname":classname,"student ID":stu_id,"student_name":studname} 


