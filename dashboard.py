import data

class Dashboard(data.Data):
    def start(self,action):
        
        if action==1:
            self.listPersons()
        elif action == 2:
            name    = input("Name : ")
            subname = input("Subname : ")
            email   = input("Email : ")
            job     = input("Job : ")
            self.insertPerson(name,subname,email,job)
            self.listPersons()
        elif action == 3:
            self.dropTablePersons()
        elif action == 4:
            self.createTablePersons()
        elif action == 5:
            self.listTables()
        else:
            print("Please insert a valid action")
            
    def listPersons(self):
        persons  = self.getPersons()
        print("Id | Name | Subname | Email | Job")
        if len(persons) == 0:
            print(" -- | -- | -- | --")
        for row in persons:
            print(str(row[0]) +" | "+ str(row[1]) +" | "+ str(row[2]) +" | "+ str(row[3]) +" | "+ str(row[4]) )
            
    def insertPerson(self,name,subname,email,job):
        
        datas   ={
            "name":name,
            "subname":subname,
            "email":email,
            "job":job
        }
        
        self.addPerson(datas)