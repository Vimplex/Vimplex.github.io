from flask import session, g, request, redirect
from flask import render_template, url_for
from MySite.app import app

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/')
def index():
    from .models import Apps
    Apps()
    
    raw_apps = Apps().get_apps()
    last = []
    test = len(raw_apps)%3
    if test == 0:
        apps = raw_apps
    elif test == 1:
        last.append(raw_apps.pop())
        apps = raw_apps
    else:
        last.append(raw_apps.pop())
        last.append(raw_apps.pop())
        apps = raw_apps
    print(test)
    print(len(apps))
    print(last)
   
    if 'user' in session and session['logged_in'] == True:
        user = session['user']
        return render_template('index.html', user=user, apps=apps, last=last)
    return render_template('index.html', apps=apps, last=last)

@app.route('/signup', methods=['GET', 'Post'])
def signup():
    if request.method == 'POST':
        
        if request.form['s'] == 's':
            uid = request.form['uid']
            passion = request.form['passion']
            pwd = request.form['pwd']
            conf_pwd = request.form['conf_pwd']
            # Error handler
            error = {}
            if len(uid) >= 3 and passion != 0 and len(pwd) >= 5 and pwd == conf_pwd:
                from .models import User
                if User(uid).find_user():
                    error['uid'].append('user already exists')
                    print (error)
                User(uid).register(passion, pwd)
                session['user'] = uid
                session['logged_in'] = True
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['l']:
            uid = request.form['uid']
            pwd = request.form['pwd']
            if len(uid) < 3 or len(uid) > 55:
                error = True 
            elif len(pwd) < 5:
                error = True
            else:
                from .models import User
                if not User(uid).login(pwd):
                    error = True
                else:
                    session['user'] = uid
                    session['logged_in'] = True
    return redirect('/')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    print(session['user'])
    session.pop('user')
    session['logged_in'] = False
    return redirect('/')

@app.route('/add_apps', methods=['GET', 'POST'])
def add_apps():
    if request.method == 'POST':
        if request.form['s'] == 's':
            url = request.form['url']
            title = request.form['title']
            subtitle = request.form['subtitle']
            desc = request.form['desc']
            from .models import Admin
            Admin().add_apps(url, title, subtitle, desc)
        
    return redirect('/')

@app.route('/start')
def start():
    return 'Here will be the start'
