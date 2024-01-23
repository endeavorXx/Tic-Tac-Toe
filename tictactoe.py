import random as rn
import database as db
from pwinput import pwinput

class Players:
    def __init__(self):
        self.username = ""
        self.age = ""
        self.pswd = ""
        self.mobile = ""
        self.win = 0
        self.loss = 0
        self.draw = 0
        Players.intro(self)

    def intro(self):
        print("                             WELCOME TO TIC-TAC-TOE PORTAL               ")
        menu = input("""
1.Enter 1 to login
2.Enter 2 to signup:""")
        
        if menu == "1":
            Players.login(self)
        elif menu == "2":
            Players.signup(self)

    def login(self):
        print("Welcome to login portal")
        count = 1
        while True:
            user = input("Enter Username:")
            pswd = pwinput("Enter password:","*")
            if count>=3:
                ch = input("Forgot Password?\nEnter 1 reset:")
                if ch=="1":
                    Players.changedetails(self)
                    break
            if db.checkinfo(user,pswd):         ##check details of the user in database
                if user not in playerl:
                    playerl.append(user)
                    print("Welcome",user)
                elif user in playerl:
                    print("Same User!!")
                    Players.intro(self)
                break
            else:
                print("Incorrect username or password")
                count+=1

    def signup(self):
        print("Signup Here")
        while True:
            username = input("Enter username:")     ##check if username exists or not
            if db.userinfo(username):
                print("Username already taken!!\nEnter Again :)")
            else:
                break

        age = input("Enter your age:")
        while True:
            mob = input("Enter your mobile number:")
            if db.checkmob(mob):
                print("Wrong Mobile number entered!!")
                print()
            else:
                break
        while True:
            pswd = pwinput("create password:","*")
            retype = pwinput("Retype password:","*")
            if pswd!=retype:
                print("Incorrect password!! Enter Again :) ")
                print()
            else:
                break
        db.uploaddata(username,age,mob,pswd)        ##save details to the database
        print("----------------Username created-----------------")
        print()
        Players.login(self)
    
    def changedetails(self):
        while True:
            mob = input("Enter your mobile number:")
            if db.checkmob(mob):
                while True:
                    newuser = input("Create username:")     ##check if username exists or not
                    if db.userinfo(newuser):
                        print("Username already taken!!\nEnter Again :)")
                    else:
                        break
                while True:
                    newpass = pwinput("Enter new password:")
                    retype = pwinput("Re-Enter password:")
                    if newpass==retype:
                        break
                    else:
                        print("wrong password enter again :)")
                db.changeinfo(newuser,newpass,mob)
                print("Data Uploaded!!\nPlease login again :)")
                print()
                Players.login(self)
                break
            else:
                print("Mobile Number not in records !!")
                Players.intro()
                break       

playerl = []
for i in range(2):
    Players()

print(playerl)

def winner(l):
    if l[0][0]==l[0][1] and l[0][1]==l[0][2] and l[0][0]!=None and l[0][1]!=None and l[0][2]!=None:
        return True
    elif l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]!=None and l[1][0]!=None and l[2][0]!=None:
        return True
    elif l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[0][0]!=None and l[1][1]!=None and l[2][2]!=None:
        return True
    elif l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][0]!=None and l[1][1]!=None and l[1][2]!=None:
        return True
    elif l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][0]!=None and l[2][1]!=None and l[2][2]!=None:
        return True
    elif l[2][0]==l[1][1] and l[1][1]==l[0][2] and l[2][0]!=None and l[1][1]!=None and l[0][2]!=None:
        return True
    elif l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[0][1]!=None and l[1][1]!=None and l[2][1]!=None:
        return True
    elif l[0][2]==l[1][2] and l[1][2]==l[2][2] and l[0][2]!=None and l[1][2]!=None and l[2][2]!=None:
        return True
    else:
        return False
def matrix(list):
    for i in list:
        print(i)
def row(num):
    return int(num//10)
def column(num):
    return int(num%10)
l = [[None for i in range(3)] for j in range(3)]
count = 0
lst,dic = [],{}
stndrdlst = [11,12,13,21,22,23,31,32,33]
playerA = rn.randint(0,1)
if playerA == 1:
    playerA = "x"
    playerB = "0"
else:
    playerA = "0"
    playerB = "x"
print("                         START TIC_TAC_TOE            ")
print()
print('''Game rules:
1.Each player will be alloted 0 or x
2.player has to enter the position where he wants to place 0\\x
3.position entered is as per the rules of row-column position in a matrix
4.A typical example for positions in a matrix are : \n[\"11\",\"12\",\"13\"]\n[\"21\",\"22\",\"23\"]\n[\"31\",\"32\",\"33\"]
''')
a = playerl[0]
b = playerl[1]
print(f"\"{a} got {playerA} and {b} got {playerB}\"")
print()
while True:
    if count%2==0:
        print(f"{a} turn you got {playerA}\n")
        matrix(l)
        print("----------------")
        while True:
            num = int(input("Enter index:"))
            if num not in stndrdlst:
                print("Invalid Input :) please Enter again!!")
            else:
                if num not in lst:
                    lst.append(num)
                    break
                else:
                    print("Index alredy occupied :) please enter again!!")
        print("----------------")
        lst.append(num)
        i,j = row(num),column(num)
        l[i-1][j-1] = playerA
        win1 = winner(l)
        if win1:
            print(f"{a} won the game")
            dic = {f"{a}":"win",f"{b}":"loss"}
            matrix(l)
            break
    else:
        print(f"{b} turn you got {playerB}\n")
        matrix(l)
        print("------------------")
        while True:
            num = int(input("Enter index:"))
            if num not in stndrdlst:
                print("Invalid Input :) please Enter again:")
            else:
                if num not in lst:
                    lst.append(num)
                    break
                else:
                    print("Index alredy occupied :) please enter again!!")
        print("------------------")
        lst.append(num)
        i,j = row(num),column(num)
        l[i-1][j-1] = playerB
        win2 =winner(l)
        if win2:
            print(f"{b} won the game")
            dic = {f"{a}":"loss",f"{b}":"win"}
            matrix(l)
            break
    if count==8:
        print("Match draw")
        dic = {f"{a}":"draw",f"{b}":"draw"}
        matrix(l)
        break
    count+=1
    print()

for key in dic:
    print("true")
    if dic[key]=="win":
        db.addwin(key)
    if dic[key]=="loss":
        db.addloss(key)
    if dic[key]=="draw":
        db.adddraw(key)
while True:
    menu = input("""
    1.Enter 1 to show records of a username
    2.Enter 2 to show Rankings
    3.Enter 0 to exit:
    """)
    if menu=="1":
        while True:
            user = input("Enter username:")
            if db.userinfo(user):
                data = db.getuser(user)
                print(data)
                break
            else:
                print("Incorrect Username")
    elif menu=="2":
        count  = 1
        data = db.getdata()
        print("     NAME AGE WIN")
        for row in data:
            print(f"{count}:{row}")
            count+=1
    elif menu=="0":
        break