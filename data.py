
import connection

class Data(connection.Connection):
    
    def getPersons(self):
        sql = "SELECT * FROM persons ORDER BY id DESC"
        self.Db.execute(sql)
        return self.Db.fetchall()
    def addPerson(self,data):
        sql = "INSERT INTO persons(name,subname,email,job) VALUES(%s,%s,%s,%s)"
        values = (
            data.get("name"),
            data.get("subname"),
            data.get("email"),
            data.get("job")
        )
        self.Db.execute(sql,values)
        self.Instancedb.commit()
        
    def listTables(self):
        t_list = self.getTables()
        for row in t_list:
            print("Name | " + str(row[0]))