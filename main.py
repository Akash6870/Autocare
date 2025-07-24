from flask import*
from public import public
from admin import admin
from shop import shop
from api import api

app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(shop)
app.secret_key="ibrahim"
app.register_blueprint(api)

app.run(debug=True,port=5007,host="0.0.0.0")