import os
import sys
#sys.path.insert(0,'/home/robertspartacus/public_html/equalto/myenv/lib/python2.6/site-packages')
import json,cgi,re,time
from flask import Flask, render_template, session, redirect, url_for, request,jsonify, flash
from flask_oauth import OAuth
import urllib2
from flaskext.mysql import MySQL #comment this line when used in cpanel
#from flask.mysql import MySQL     #enable this line when used in cpanel
from urllib2 import Request, urlopen, URLError
#OAuth configurations
GOOGLE_CLIENT_ID = '281438845469-1stqnv392m59mev23hb7i7cqeq6td69v.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'RWmu3o1JvRvHYgvD-Xg2oz_F'
REDIRECT_URI = '/oauth2callback'
SECRET_KEY = 'the key to secret'

app = Flask(__name__)
app.secret_key = SECRET_KEY
if app.debug is not True:   
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('rkerrorlog.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

oauth = OAuth()
mysql = MySQL()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)
 
# MySQL configurations #change the user and password when used in cpanel

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'equalto'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)



@app.route('/')
def timer():
  return render_template('baseBeforeRun.html')

if __name__=='__main__':
  app.run('127.0.0.1',5000,True)