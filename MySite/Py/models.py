import time
import csv
from hashlib import sha1




class User:

    def __init__(self, uid):
        from .DB.mlab_connect import mongo
        self.mongo = mongo
        self.uid = uid
    
    def register(self, passion, pwd):
        h_pwd = sha1(str.encode(str(pwd))).hexdigest()
        timestamp = time.time()
        if self.uid != 'Admin':
            user = self.mongo.db.user
            user.insert({'uid':self.uid, 'passion':passion, 'pwd': h_pwd, 'timestamp':timestamp})
        else:
            admin = self.mongo.db.admin
            admin.insert({'uid':self.uid, 'passion':passion, 'pwd': h_pwd, 'timestamp':timestamp})

    def login(self, pwd):
        if self.uid != 'Admin':
            user = self.find_user()
            if user:
                if user['pwd'] == sha1(str.encode(str(pwd))).hexdigest():
                    return True
            return False
        else:
            admin = self.mongo.db.admin.find_one({'uid':'Admin'})
            print(admin)
            if admin:
                if admin['pwd'] == sha1(str.encode(str(pwd))).hexdigest():
                    return True
            return False

    def find_user(self):
        result = self.mongo.db.user.find_one({'uid':self.uid})
        try:
            if len(result) == 5:
                return result
        except:
            return False

class Admin:
    def add_apps(self, url, title, subtitle, desc):
        with open('MySite/Py/apps.csv', 'a') as f:
            fieldnames = ['url', 'title', 'subtitle', 'description']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow({'url':url, 'title': title, 'subtitle': subtitle, 'description':desc})

class Apps:
    def get_apps(self):
        apps = []
        with open('MySite/Py/apps.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                apps.append({'url':row[0], 'Name': row[1], 'subtitle': row[2], 'description': row[3]})
        return apps
    
    
    def add_app(self, Name, subtitle, desc, url):
        app = {'Name': Name, 'subtitle':subtitle, 'description':desc, 'url':url}
        self.apps.append(app)
