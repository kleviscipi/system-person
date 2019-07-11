import mysql.connector as dbconnect

class Connection:
    def __init__(self):
       self.getInstanceLive()
       
    def getInstanceLive(self):
        self.Instancedb = self.getInstance()
        
        if self.Instancedb.is_connected:
            cursor  = self.Instancedb.cursor()
            self.Db =  cursor
            if self.existPersonsTable() ==False:
                self.createTablePersons()
            return self.Instancedb
        else:
            cursor  = self.Instancedb.cursor()
            self.Db =  cursor
            self.createDb()
            self.Instancedb = self.getInstance()
            return self.Instancedb

    def getInstance(self):
        return dbconnect.connect(
            host="localhost",
            user="root",
            passwd="",
            database="system_person"
        )
    def getTables(self):
        self.Db.execute("SHOW TABLES")
        return self.Db.fetchall()
    
    def existPersonsTable(self):
        t_list = self.getTables()
        exist = False
        for row in t_list:
            if row[0] == "persons":
                exist = True
            break;
        return exist
    def createDb(self):
        try:
            sql = "CREATE DATABASE IF NOT EXISTS system_person"
            self.Db.execute(sql)
            self.Instancedb.commit()
            print("Success")
        except:
            print("Something goes wrong")
        finally:
            print("Action Create DB End")
        
    def dropTablePersons(self):
        try:
            self.Db.execute("DROP TABLE IF EXISTS persons");
            print("Success")
        except:
            print("Something goes wrong")
        finally:
            print("Action Drop Table Persons End")
            
    def createTablePersons(self):
        sql = """
            CREATE TABLE IF NOT EXISTS persons(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                subname VARCHAR(100),
                email VARCHAR(100),
                job VARCHAR(100)
            ); 
        """
        try:
            if self.existPersonsTable() == True:
                print("Table Exist, Skip")
            else:
                self.Db.execute(sql)
                self.Instancedb.commit()
                print("Success")
        except:
            print("Something goes wrong")
        finally:
            print("Action Create Table Persons End")

            