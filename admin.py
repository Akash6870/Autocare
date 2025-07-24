from flask import*
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhouse():
    return render_template('adminhome.html')

@admin.route('/verify_shop')
def verify_shop():  
    data={}
    xyz="select * from shop"
    res=select(xyz)
    data['r']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if 'action'=='accept':
            qry="update login set usertype='shop' where shop_id='%s'"%(id)
            update(qry)
            if action=='reject': 
                qry1="delete shop set usertype='shop' where shop_id='%s'"%(id)
                delete(qry1)

    return render_template('verify_shop.html',data=data)

@admin.route('/screg',methods=['post','get'])
def service_center():
    block={}
    xyz="select * from service_center"
    res=select(xyz)
    block['r']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action=='delete':
            qry1="delete from service_center where login_id='%s'"%(id)
            delete(qry1)
            return '''<script>alert('Deleted');window.location='/screg'</script>'''
        if action=='update':
            qry="select * from service_center where service_center_id='%s'"%(id)
            res=select(qry)
            block['view']=res

    if 'submit' in request.form:
        
        name=request.form['name']
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['uname']
        password=request.form['psw']

        a="insert into login values(null,'%s','%s','service_center')"%(username,password)
        id=insert(a)
        
        b="insert into service_center values(null,'%s','%s','%s','%s','%s','%s')"%(name,latitude,longitude,phone,email,id)
        insert(b)
        return '''<script>alert('registered');window.location='/screg'</script>'''
    return render_template('service_center.html',block=block)

@admin.route('/mechanic',methods=['post','get'])
def mechanic():
    abc={}
    xyz="select * from mechanic"
    res=select(xyz)
    abc['r']=res

    if 'submit' in request.form:
                name=request.form['name']
                latitude=request.form['latitude']
                longitude=request.form['longitude']
                phone=request.form['phone']
                email=request.form['email']

                a="insert into mechanic values(null,'%s','%s','%s','%s','%s')"%(name,latitude,longitude,phone,email)
                insert(a)


    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

        if action=='delete':
            qry="delete from mechanic where mechanic_id='%s'"%(id)
            delete(qry)
            return '''<script>alert('deleted');window.location='/mechanic'</script>'''
        
        if action=='update':
            qry2="select * from mechanic where mechanic_id='%s'"%(id)
            res=select(qry2)
            abc['view']=res

            if 'submit' in request.form:
                name=request.form['name']
                latitude=request.form['latitude']
                longitude=request.form['longitude']
                phone=request.form['phone']
                email=request.form['email']

                a="insert into mechanic values(null,'%s','%s','%s','%s','%s')"%(name,latitude,longitude,phone,email)
                insert(a)

                return '''<script>alert('registered');window.location='/mechanic'</script>'''
    return render_template('mechanic.html',abc=abc)

@admin.route('/vehicle_type',methods=['get','post'])
def vehicle_type():
    pqr={}
    rqp="select * from vehicle_type"
    res=select(rqp)
    pqr['rrr']=res

    

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
         action=None

    if action=='delete':
            qry1="delete from vehicle_type where vehicle_type_id='%s'"%(id)
            delete(qry1)

            return '''<script>alert('deleted');window.location='/mechanic'</script>'''
    if action=='update':

            qry2="select * from vehicle_type where vehicle_type_id='%s'"%(id)
            res=select(qry2)
            pqr['view']=res

    if 'submit' in request.form:

        typename=request.form['typename']

        a="insert into vehicle_type values(null,'%s')"%(typename)
        insert(a)

        return '''<script>alert('registered');window.location='/vehicle_type'</script>'''
    return render_template('vehicle_type.html',pqr=pqr)

        

    