from flask import Flask
from mongoengine import connect

app = Flask(__name__)

app.config["MONGODB_DB"] = 'app12345678'
connect(
    'app12345678',
    username='heroku',
    password='a614e68b445d0d9d1c375740781073b4',
    host='mongodb://<user>:<password>@alex.mongohq.com:10043/app12345678',
    port=10043
)
if __name__=='__main__':
    app.run()