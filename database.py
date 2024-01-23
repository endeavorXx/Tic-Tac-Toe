import mysql.connector as sql
mycon = sql.connect(host="localhost",user="root",password="123456",auth_plugin = "mysql_native_password")
cursor = mycon.cursor()

def execute(string):
    cursor.execute(string)

execute("use tictactoe")

def uploaddata(username,age,mobile,pswd):
    execute("use tictactoe")
    data = "INSERT INTO GAME(USERNAME,AGE,MOBILE,PASSWORD) VALUES ('{}','{}','{}','{}')".format(username,age,mobile,pswd)
    execute(data)
    mycon.commit()

def userinfo(username):
    execute("select username from game")
    data = cursor.fetchall()
    lst = []
    for row in data:
        for i in row:
            lst.append(i)
    if username in lst:
        return True
    else:
        return False


def checkinfo(user,pswd):
    execute("select username,password from game")
    data = cursor.fetchall()
    flag = 0
    for row in data:
        if row[0]==user and row[1]==pswd:
            flag=1
    if flag==1:
        return True
    else:
        return False
def checkmob(mob):
    execute("select mobile from game")
    data = cursor.fetchall()
    flag = 0
    for row in data:
        if row[0]==mob:
            flag=1
    if flag==1:
        return True
    else:
        return False

def changeinfo(user,pswd,mobile):
    execute("update game set username='{}',password='{}' where mobile='{}'".format(user,pswd,mobile))
    mycon.commit()

def addwin(user):
    execute("select win from game where username='{}'".format(user))
    data = cursor.fetchall()
    data = data[0][0]+1
    execute("update game set win='{}' where username='{}'".format(data,user))
    mycon.commit()

def addloss(user):
    execute("select loss from game where username='{}'".format(user))
    data = cursor.fetchall()
    data = data[0][0]+1
    execute("update game set loss='{}' where username='{}'".format(data,user))
    mycon.commit()

def adddraw(user):
    execute("select draw from game where username='{}'".format(user))
    data = cursor.fetchall()
    data = data[0][0]+1
    print(data)
    execute("update game set draw='{}' where username='{}'".format(data,user))
    mycon.commit()

def getuser(user):
    execute("select win,loss,draw from game where username='{}'".format(user))
    data = cursor.fetchall()
    tot = data[0][0]+data[0][1]+data[0][2]
    dic = {"win":data[0][0],"loss":data[0][1],"draw":data[0][2],"Total Matches":tot}
    return dic

def getdata():
    execute("select username,age,win from game order by win desc,loss asc;")
    data = cursor.fetchall()
    return data

