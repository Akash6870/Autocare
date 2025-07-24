from flask import *

from database import *

api=Blueprint("api",__name__)

@api.route("/user_reg")
def user_reg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    uname=request.args['uname']
    psw=request.args['psw']

    a="insert into login values(null,'%s','%s','user')"%(uname,psw)
    id=insert(a)

    b="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
    rf=insert(b)

    if rf:
        data['status']='success'

    else:
        data['status']='failed'
    
    return str(data)

    


@api.route("/user_login")
def user_login():
    value={}

    username=request.args['username']
    pwd=request.args['pwd']
    qwy="select * from login inner join user using(login_id) where username='%s' and password='%s'"%(username,pwd)
    res=select(qwy)

    if res:
        value['status']='success'
        value['data']=res

    else:
        value['status']='failed'
    
    return str(value)

