from flask import*
from database import*

shop=Blueprint('shop',__name__)



@shop.route('/shophome')
def shopname():
    return render_template('shophome.html')

@shop.route('/updateprofile',methods=['post','get'])
def updateprofile():
    value={}
    qry3="select * from shop inner join login using (login_id) where login_id='%s'"%(session['lid'])
    print(qry3)
    res=select(qry3)
    value['r']=res

    print(value['r'],"///////////////////////////")

   
        

    if 'update' in request.form:
        shop_name=request.form['sname']
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        phone=request.form['phone']
        email=request.form['email']
        # uname=request.form['uname']
        # psw=request.form['psw']
        

        # a="update login set username='%s',password='%s' where login_id='%s'"%(uname,psw,session['shop'])
        # update(a)

        b="update shop set shop_name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where shop_id='%s'"%(shop_name,latitude,longitude,phone,email,session['shop'])
        update(b)

    return render_template('updateprofile.html',value=value)

@shop.route('/viewvehicle_type',methods=['post','get'])
def vehicletype():
    print("////////////////////////////////////")
    data={}
    abc="select * from vehicle_type"
    res=select(abc)
    print(res,"resssssssssssssssssssssssssssssssssssssss")
    data['v_type']=res
 
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='delete':
       qry1="delete from vehicle_type where vehicle_type_id='%s'"%(id)
       delete(qry1)

       return '''<script>alert('deleted');window.location='/viewvehicle_type'</script>'''

    if action=='update':
       qry2="select * from vehicle_type where vehicle_type_id='%s'"%(id)
       res=select(qry2)   
       data['view']=res 

    return render_template('viewvehicle_type.html',data=data)  


@shop.route('/vieworder',methods=['post','get'])
def vieworder():
    valid={}
    mo="select * from order_master"
    ser=select(mo)
    valid['r']=ser

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None
        

        if action=='view':
            qry3="SELECT * FROM order_master INNER JOIN order_details USING (om_id) inner join user using(user_id) WHERE shop_id='%s' "%(id)
            valid['up']=select(qry3)


    return render_template('vieworder.html',valid=valid)




@shop.route('/vieworders',methods=['post','get'])
def vieworders():
    data={}





