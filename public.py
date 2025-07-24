from flask import*
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def welcome():
    return render_template('home.html')


@public.route('/log',methods=['get','post'])
def log():
      if 'submit' in request.form:
        uname=request.form['uname']
        psw=request.form['psw']
        qwy="select * from login where username='%s' and password='%s'"%(uname,psw)
        res=select(qwy)      
        print(res)

        if res:
            session['lid']=res[0]['login_id']
            utype=res[0]['usertype']

        if utype=="admin":
            return redirect(url_for('admin.adminhouse'))

        elif utype=="shop":
            qry="select * from shop where login_id='%s'"%(session['lid'])
            res=select(qry)
            session['shop']=res[0]['shop_id']
            return redirect(url_for('shop.shopname'))

        

      
      return render_template('login.html')

@public.route('/reg',methods=['post','get'])
def reg():
    if 'submit' in request.form:
        
        sname=request.form['sname'] 
        
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        psw=request.form['psw']

        a="insert into login values(null,'%s','%s','user')"%(uname,psw)
        id=insert(a)

        b="insert into shop values(null,'%s','%s','%s','%s','%s','%s')"%(id,sname,latitude,longitude,phone,email)
        insert(b)
        return '''<script>alert('registered');window.location='/reg'</script>'''
    return render_template("shop.html") 




  