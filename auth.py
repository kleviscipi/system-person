import os
import connection


class Auth(connection.Connection):
    def __init__(self, email="", password=""):
        if email and password:
            self.email = email
            self.password = password
            self.setAuth()
    def getEmail(self):
        return self.email
    def isLogged(self):
        file_auth = "auth_logged.txt"
        if os.path.exists(file_auth):
            auth_file_logged    = open(file_auth)
            lines           = auth_file_logged.readline(46)
            auth_email      = lines.split("(*_*)")[0].split(":")[1]
            auth_password   = lines.split("(*_*)")[1].split(":")[1]
            auth_file_logged.close()
            if auth_email and auth_password:
                self.email = auth_email
                return True
            else:
                return False
        else:
            return False
        
    def setAuth(self):
        if self.checkAuth() == True:
            auth_logged_file = open("auth_logged.txt",'w')
            auth_logged_file.write("Email:"+self.email+"(*_*)Password:"+self.password)
            auth_logged_file.close()
        else:
            print("Is not logged")
            
    def checkAuth(self):
        file_auth = "auth.txt"
        if os.path.exists(file_auth) == False:
            print("File is not found (auth.txt)")
            return False
        try:
            auth_file       = open("auth.txt")
            lines           = auth_file.readline(47)
            auth_email      = lines.split("(*_*)")[0].split(":")[1]
            auth_password   = lines.split("(*_*)")[1].split(":")[1]
            auth_file.close()
            print(self.email,auth_email)
            print(self.password,auth_password)
            if auth_password and auth_email:
                if self.email == auth_email and self.password == auth_password:
                    return True
                else:
                    return False
            else:
                return False
        except:
            print("Somthings goes wrong, please try again!")
            return False