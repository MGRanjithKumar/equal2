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

TOTAL_QUESTIONS=15
DEPENDENCY_MAP=[2,2,1,4,3,2,3,1,3,3,4,4,1,3,2]


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('baseBeforeRun.html')


@app.route('/timer')
def timer():
    return render_template('baseBeforeRun.html')

def isMailPresent(email):
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT COUNT(1) FROM HOD_vision17_users where v17Mail='%s'" % (email))
        ans=cursor.fetchall()
        con.commit()
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in isMailPresent() function:\n')
            app.logger.error(e)
        else:
            print 'Exception in isMailPresent() function:\n', e
        return 'error'
    if ans[0][0]==0:
        return False
    else:
        return True

def isGamerPresent(email):
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT COUNT(1) FROM equalto_vision17_users where email='%s'" % (email))
        ans=cursor.fetchall()
        con.commit()
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in isGamerPresent() function:\n')
            app.logger.error(e)
        else:
            print 'Exception in isGamerPresent() function:\n', e
        return 'error'
    if ans[0][0]==0:
        return False
    else:
        return True

def getCount(email):
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT count FROM equalto_vision17_users where email=%s",(email,))
        c=cursor.fetchall()
        con.commit()
        return c[0][0]
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in getCount(email) function:\n')
            app.logger.error(e)
        else:
            print 'Exception in getCount(email) function:\n', e
        return 'error'

def getEndTime(email):
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT endTime FROM equalto_vision17_users where email=%s",(email,))
        c=cursor.fetchall()
        con.commit()
        #print 'c ', c
        if c is ():
            #print 'if c none'
            return -1
        return int(c[0][0])
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in getEndTime(email) function:\n')
            app.logger.error(e)
        else:
            print 'Exception in getEndTime(email) function:\n', e  
        return 'error'

def updateScore(email):
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15 from equalto_vision17_users where email=%s",(email,))
        scores=cursor.fetchall()
        con.commit()
        #print 'scores ', scores
        scoreList=[]
        for i in range(0,15):
            if scores[0][i] is not ():
                scoreList.append(scores[0][i])
        #print scoreList
        finalScore=0
        for i in range(0,15):
            if(scoreList[i]==DEPENDENCY_MAP[i]):
                finalScore=finalScore+1
        conn=mysql.connect()
        cursorr=conn.cursor()
        cursorr.execute("UPDATE equalto_vision17_users set score=%d WHERE email='%s'" % (finalScore,email))
        conn.commit()
        return finalScore
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in updateScore(email) function:\n')
            app.logger.error(e)
        else:
            print 'Exception in updateScore(email) function:\n', e  
        return 'error'

def insertIntoSQL(name,email,mobile,college,year,department,othercollege,imageurl):
    name=cgi.escape(name,quote=True)
    college=cgi.escape(college,quote=True)
    year=cgi.escape(year,quote=True)
    othercollege=cgi.escape(othercollege,quote=True)
    department=cgi.escape(department,quote=True)
    match_num=re.search(r'(\d{10})',str(mobile))
    if match_num is None:
        return 'error'
    mobile=int(match_num.group())
    cursor=mysql.connect().cursor()
    vid=queryMaxId()+1
    v17Id='v'+str(vid)
    try:
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("INSERT INTO HOD_vision17_users(v17Id,id,v17Name,v17Mail,v17Mobile,v17College,v17Year,v17Department,v17CollegeOther,v17SA,v17Image,v17Subscriptions) VALUES ('%s',%d,'%s','%s',%d,'%s','%s','%s','%s','vNONE','%s','Yet')" % (v17Id,vid,name,email,mobile,college,year,department,othercollege,imageurl))
        if cursor.fetchall() is None:
            return True
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in isMailPresent() function:\n')
            app.logger.error(e)
        else:
            print 'Exception in isMailPresent() function:\n', e
        return 'error'


def queryMaxId():
    cursor=mysql.connect().cursor()
    try:
        cursor.execute("SELECT max(id) from HOD_vision17_users")
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in queryMaxId() function\n')
            app.logger.error(e)
        else:
            print 'Exception in queryMaxId() function:\n', e
        return 'error'
    maxId=cursor.fetchall()
    if maxId is None:
        return 'error'
    return maxId[0][0]

def getVID(email):
    cursor=mysql.connect().cursor()
    try:
        cursor.execute('SELECT v17Id from HOD_vision17_users where v17Mail="%s"' % (email))
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in getVID(email) function:\n')
            app.logger.error(e)
        else:
            print 'Exception in getVID(email) function:\n', e
        return False
    v17Id=cursor.fetchall()
    if v17Id is None:
        return False
    else:
        return v17Id[0][0]

def getDetails():
    access_token = session.get('access_token')
    try:
        access_token = access_token[0]
        headers = {'Authorization': 'OAuth '+access_token}
        req = Request('https://www.googleapis.com/oauth2/v1/userinfo',None, headers)
        res = urlopen(req)
        jsonstri=json.loads(res.read().decode('utf-8'))
        return jsonstri
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in getDetails() function\n')
            app.logger.error(e)
        else:
            print 'Exception in getDetails() function:\n', e
        return 'error'

def isGameAlive(email):
    utcTime=int(time.time())
    endTime=getEndTime(email)
    try:
        if utcTime > endTime:
            return False
        else:
            return True
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in getDetails() function\n')
            app.logger.error(e)
        else:
            print 'Exception in getDetails() function\n', e
        return redirect(url_for('main'))


@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        access_token = session.get('access_token')
        ##print 'Entering check'
        if access_token is None:
            ##print 'Entering if'
            atoken="none"
            name=''
            picture=''
            # flash('You are not logged in')
            return render_template('index.html',atoken=atoken,name=name,picture=picture,utcEndTime=-1)
        else:
            ##print 'Entering else'
            atoken=access_token[0]
            jsonstri=getDetails()
            if jsonstri=='error':
                session.pop('access_token', None)
                return redirect(url_for('login'))
            elif isGamerPresent(jsonstri['email']):
                return redirect(url_for('game'))
            else:
                return render_template('index.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],utcEndTime=getEndTime(jsonstri['email']))

    else:
        access_token = session.get('access_token')
        if access_token is None:
            return redirect(url_for('login'))
        atoken = access_token[0]
        jsonstri=getDetails()
        if jsonstri=='error':
            session.pop('access_token', None)
            return redirect(url_for('login'))
        elif isGamerPresent(jsonstri['email']):
            return redirect(url_for('game'))
        else:
            return render_template('index.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],utcEndTime=getEndTime(jsonstri['email']))

@app.route('/updateEveryonesScore2013105050')
def evaluateEveryOnesScore():
    try:
        utcTime=int(time.time())
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT email from equalto_vision17_users where score = 0 and endTime < %d" % (utcTime,))
        listUpdates=cursor.fetchall()
        con.commit()
        for gamer in listUpdates: 
            updateScore(gamer[0])
        return 'updated score for :' + str(listUpdates)
    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in isMailPresent() function:\n')
            app.logger.error(e)
        else:
            print 'Exception in isMailPresent() function:\n', e

@app.route('/getCurrentTime2013105050')
def getCurrentTime2013105050():
    mytime={'utcTime ': int(time.time()), 'utcOffsetTime ': int(time.time())+19800 , 'convertedUTCOffsetTime : ' : time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(time.time())+19800))}
    return str(mytime)
    #return 'time.gmtime(int(time.time())): ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(time.time())))) + '\nint(time.time()) + 19800 : ' + str(int(time.time()+19800)) + '\ntime.localtime(int(time.time())): ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))))


@app.route('/leaderboard<page>')
def leaderboard(page):
    page=int(page)
    pageLimit=10
    pageOffset=(page-1)*10
    try:
        utcTime=int(time.time())
        con=mysql.connect()
        cursor=con.cursor()
        cursor.execute("SELECT email,score from equalto_vision17_users where endTime < %d order by score desc, last_update limit %d offset %d" % (utcTime,pageLimit,pageOffset))
        leaderboard=cursor.fetchall()
        con.commit()
        #print 'leaderboard ', leaderboard
        leaderboardList=[]
        sNo=((page-1)*10)+1
        for row in leaderboard:
            leaderList={
            'sNo':sNo,
            'email':row[0],
            'score':row[1]
            }
            leaderboardList.append(leaderList)
            sNo=sNo+1
        if page is 1:
            return render_template("leaderboard.html",leaderboardList=leaderboardList,atoken='',name='',picture='',utcEndTime=-2,page=page,prev=-1,next=(page+1))
        elif len(leaderboardList) is 0:
            return render_template("leaderboard.html",leaderboardList=leaderboardList,atoken='',name='',picture='',utcEndTime=-2,page=page,prev=(page-1),next=-1)
        return render_template("leaderboard.html",leaderboardList=leaderboardList,atoken='',name='',picture='',utcEndTime=-2,page=page,prev=(page-1),next=(page+1))

    except Exception as e:
        if app.debug is not True:
            app.logger.error('Exception in leaderboard page:\n')
            app.logger.error(e)
        else:
            print 'Exception in leaderboard page :\n', e  
        return 'error'

    return render_template('leaderboard.html')

@app.route('/eventStartPage')
def eventStartPage():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('main'))
    atoken = access_token[0]
    jsonstri=getDetails()
    if jsonstri=='error':
        session.pop('access_token', None)
        return redirect(url_for('login'))
    email=jsonstri['email']
    if isGamerPresent(email)==True:
        return redirect(url_for('game'))
    elif isMailPresent(email)==True:
        return redirect(url_for('rules'))
    else:
        return render_template("register.html",atoken=atoken,name=jsonstri['name'],email=email,picture=jsonstri['picture'],utcEndTime=getEndTime(jsonstri['email']))

@app.route('/rules')
def rules():
    access_token = session.get('access_token')
    if access_token is None:
        atoken="none"
        name=''
        picture=''
        return redirect(url_for('main'))
    atoken = access_token[0]
    jsonstri=getDetails()
    if jsonstri=='error':
        session.pop('access_token', None)
        return redirect(url_for('login'))
    elif isGamerPresent(jsonstri['email']):
        return redirect(url_for('game'))
    elif isMailPresent(jsonstri['email'])==True:
        VID=getVID(jsonstri['email'])
        return render_template('rules.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],VID=VID,utcEndTime=getEndTime(jsonstri['email']))
    else:
        return redirect(url_for('eventStartPage'))

@app.route('/register', methods = ['POST'])
def register():
    access_token = session.get('access_token')
    if access_token is None:
        atoken="none"
        name=''
        picture=''
        return redirect(url_for('main'))
    atoken = access_token[0]
    jsonstri=getDetails()
    if jsonstri=='error':
        session.pop('access_token', None)
        return redirect(url_for('login'))
    else:
        name=request.form['name']
        email=jsonstri['email']
        mobile=request.form['mobile']
        college=request.form['college']
        year=request.form['year']
        department=request.form['department']
        othercollege=request.form['othercollege']
        imageurl=jsonstri['picture']
        check = insertIntoSQL(name,email,mobile,college,year,department,othercollege,imageurl)
        if check == True:
            VID=getVID(email)
            if VID is False:
                return redirect(url_for('main'))
            else:
                return redirect(url_for('rules'))
        else:
            return redirect(url_for('eventStartPage'))

@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)

@app.route('/configureGame')
def configureGame():
    access_token = session.get('access_token')
    if access_token is None:
        atoken="none"
        name=''
        picture=''
        return redirect(url_for('main'))
    atoken = access_token[0]
    jsonstri=getDetails()
    if jsonstri=='error':
        session.pop('access_token', None)
        return redirect(url_for('login'))
    elif isGamerPresent(jsonstri['email'])==True:
        return redirect(url_for('game'))
    elif isMailPresent(jsonstri['email'])==True:
        try:
            conn = mysql.connect()
            cursor=conn.cursor()
            #print 'calling callproc'
            utcTime=int(time.time())
            cursor.callproc('initializeUser',(jsonstri['email'],utcTime,(utcTime+1800)))
            received = cursor.fetchall()
            #print 'len received'
            #print len(received)
            if len(received) is 0:
                conn.commit()
                return redirect(url_for('game'))
            else:
                return redirect(url_for('rules'))
        except Exception as e:
            #print "Exception: ", e
            return redirect(url_for('rules'))
    else:
        return redirect(url_for('eventStartPage'))
 
@app.route('/game', methods = ['GET', 'POST'])
def game():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('main'))
    atoken = access_token[0]
    jsonstri=getDetails()
    #print 'jsonstri', jsonstri
    if jsonstri=='error':
        session.pop('access_token', None)
        return redirect(url_for('login'))
    else:
        utcEndTime=getEndTime(jsonstri['email'])
        if isGamerPresent(jsonstri['email'])==True:
            count=getCount(jsonstri['email'])
            if count==TOTAL_QUESTIONS or not(isGameAlive(jsonstri['email'])):
                finalScore=updateScore(jsonstri['email'])
                return render_template("success.html",atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=1,tq=TOTAL_QUESTIONS,utcEndTime=0,finalScore=finalScore)
            elif request.method == 'GET' and count==0:
                return render_template('q1.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=1,tq=TOTAL_QUESTIONS,utcEndTime=utcEndTime)
            elif request.method=='GET' and isGameAlive(jsonstri['email']):
                return render_template('q'+str(count+1)+'.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=count+1,tq=TOTAL_QUESTIONS,utcEndTime=utcEndTime)
            else:
                ans = request.form['radio']
                q = request.form['qn_number']
                ans=int(ans)
                q=int(q)
                count = getCount(jsonstri['email'])
                if((count+1)==q):
                    try:
                        conn=mysql.connect()
                        cursor = conn.cursor()
                        qno='q'+str(q)
                        cursor.execute("UPDATE equalto_vision17_users set %s=%d, count=count+1 WHERE email='%s' and %s is null" % (qno,ans,jsonstri['email'],qno))
                        conn.commit()
                    except Exception as e:
                        return render_template('q'+str(count+1)+'.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=count+1,tq=TOTAL_QUESTIONS,utcEndTime=utcEndTime)
                    if(count+1==TOTAL_QUESTIONS):
                        finalScore=updateScore(jsonstri['email'])
                        return render_template('success.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],utcEndTime=0,finalScore=finalScore)
                    else:
                        return render_template('q'+str(count+2)+'.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=count+2,tq=TOTAL_QUESTIONS,utcEndTime=utcEndTime)
                return render_template('q'+str(count+1)+'.html',atoken=atoken,name=jsonstri['name'],picture=jsonstri['picture'],qn_number=count+1,tq=TOTAL_QUESTIONS,utcEndTime=utcEndTime)
        
        else:
            return redirect(url_for('rules')) 

@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('main'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('main'))

@app.errorhandler(404)
def error404(error):
    if app.debug is not True:
        app.logger.error(error)
    return render_template('404.html'), 404

@app.route('/404')
def error404():
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(exception):
    if app.debug is not True:
        app.logger.error(error)
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run('127.0.0.1',5000,True)
