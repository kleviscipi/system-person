import auth as A
import dashboard as D

print("################################### HELLO :) #####################################")

Auth = A.Auth()
Is_LoggedBefore = Auth.isLogged()

if Is_LoggedBefore == False:
    input_user_email = input("Your Email: ")
    print("Nice to meet you " + str(input_user_email))
    input_user_password = input("Insert your pass now: ")

    print("Your Data:")
    print("Email:" + str(input_user_email))
    print("Password:" + str(input_user_password))
    print("Proceding to auth ........")

    Auth = A.Auth(input_user_email,input_user_password)

    is_logged = Auth.isLogged()

if Is_LoggedBefore or is_logged:
    print("################################### WELCOME :) ######################################")
    print("                                "+Auth.getEmail()+"                                  ")
    print("#                                                                                   #")
    print("#                                                                                   #")
    print("#                                                                                   #")
    print("#                                       AI                                          #")
    print("#                                                                                   #")
    print("#                                                                                   #")
    print("#                                                                                   #")
    print("#####################################################################################")
    print("Use an action:")
    
    print("1 ) List Persons")
    print("2 ) Insert a Persons")
    print("3 ) Drop Table Persons")
    print("4 ) Create Table Persons")
    print("5 ) List Tables")
    
    action = input()
    
    Dashboard = D.Dashboard()
    Dashboard.start(action)
    