import re
def reg():
  while True:
    print("*********User Registration**********")
    un = input("Create your user name(user must be your Email ID) : ")
    username = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w[a-z]+[.]\w{2,3}$"
    if not re.search(username, un):
        print("Enter a valid username/email ID")
        continue
    pwd = input("Create password: ")
    password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    if not re.search(password, pwd):
        print("""Enter a valid password and re-try
        {your password must contain at least one uppercase,one lower case,
        one digit and one special character, 
        length of your password should be between 5 and 16}""")
        continue
    conf_pwd = input("confirm password :")
    f = open("credentials.txt", "r")
    d=[]
    for i in f:
        a,b = i.split(",")
        b=b.strip()
        c=a,b
        d.append(a)
    if un and pwd in f:
            print("user name and password exists please try with new one or login")
            home()
    else :
      if  pwd==conf_pwd:
          f= open("credentials.txt", "a")
          f.write(un+","+pwd+"\n")
          f.close()
          print("You have registered successfully!")
          print("please login to proceed ")
          home()

      else:
          print("Password is not same as above! retry \n")
          continue

def login():
  while True:
    print("*********User Login**********")
    un = input("Enter the user name : ")
    pwd = input("Enter password:")
    if not len(un or pwd)<1:
        if True:
            f=open("credentials.txt", "r").readlines()
            d=[]
            dp=[]
            for i in f:
                a,b=i.split(",")
                b=b.strip()
                c=a,b
                d.append(a)
                dp.append(b)
                db=dict(zip(d,dp))
            try:
              if a in c :
                 hasg=db[un].strip('b')
                 try:
                    if pwd==hasg:
                        print("Logged in Successfully!")
                        print("welcome!")
                        break
                    else:
                      print("wrong password")

                 except:
                   print("incorrect password or user name")
              else:
                 print("Username does not Exists")

            except:
               print("Password or Username does not exists")
        else:
          print("Error in login")
    else:
      print("Please login again \n")
      reg()
def home():
 while True:
    print("********** Basic Login and Registration System **********")
    print("Welcome ,Please select an option")
    option = input("Login|Registration:")
    if option == "Login":
        login()
    elif option == "Registration":
        reg()
    else:
        print("Please enter a valid option")
        continue


home()