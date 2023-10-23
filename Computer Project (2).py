#project work

#establishing connectivity
import mysql.connector 
c=mysql.connector.connect(host="localhost",user="root",passwd="asdfg",charset="utf8",database="comp_project")
mycur=c.cursor()
price={1:6700,2:5000,3:9000,4:7300}


#function1 - to display schemes
def scheme():
    myfile=open(r"C:\Users\DELL\Desktop\Aarohi\scheme heading.txt","r")
    string=myfile.read()
    print(string)


#function2 - detailed scheme description
def scheme_no(x):
    while True:
            if x==1:
                myfile=open(r"C:\Users\DELL\Desktop\Aarohi\scheme1.txt","r")
                string=myfile.read()
                print(string)
                break
            elif  x==2:
                myfile=open(r"C:\Users\DELL\Desktop\Aarohi\scheme2.txt","r")
                string=myfile.read()
                print(string)
                break
            elif x==3:
                myfile=open(r"C:\Users\DELL\Desktop\Aarohi\scheme3.txt","r")
                string=myfile.read()
                print(string)
                break
            elif x==4:
                myfile=open(r"C:\Users\DELL\Desktop\Aarohi\scheme4.txt","r")
                string=myfile.read()
                print(string)
                break


#Function3 - Form
def form(schemeno):
    name=input("Enter your name\n ")
    
    while True:
        try:
            age=int(input("Enter your age\n"))
            break
        except:
            print("Invalid input\n")
            continue

    while True:
        mobn=input("Enter registered mobile number\n")
        if len(mob)==10:
            mobno=int(mob)
            break
        else:
            print("Invalid mobile number.Enter again.\n")
            continue
    print("""MODE TO TRANSPORT:

                    1. Railway(rajdhani)
                            a -  3AC train journey
                            b -  2AC train journey

                    2. Via flight\n""")
    while True:
        mode=input("Enter the mode of travelling you prefer(eg: 1a, 1b, 2)\n")
        mode=mode.lower()
        if mode=="1a" or mode=="1b" or mode=="2":
            break
        else:
            print("Invalid input.enter again\n")
            continue

    while True:
        gender=input("Gender( F / M  /  OTHER )\n")
        gender=gender.lower()
        if gender != "f" and gender != "m" and gender != "other" :
            print("Invalid input\n")
            continue
        else:
            break

    while True:
        group=input("Are you travelling in a group?(yes/no):\n")
        group=group.lower()
        if group=="yes":
            num=int(input("Number of people travelling:\n"))
            break
        elif group=="no":
            num=1
            int(num)
            remarks=input("Do you have any specification? if no fill \"none\"\n")
            break
        else:
            print("Invalid input\n")
            continue
        
    while True:
        date=input("From the given dates in schemes select trip number(corresponding date of travel will be booked)\n")
        if date>='1' and date<='5':
            break
        else:
            print("Invalid input. Enter agaian")
            continue
        break
    string="INSERT INTO schemes(mobno,schemeinfo,num,mode,date) VALUES({},{},{},'{}','{}')".format(mobno,schemeno,num,mode,date)
    mycur.execute(string)
    c.commit()
    return(num,mode)


#function4 - billing
def bill(x,num,mode):
    per=price[x]
    int(per)
    num1=num
    print("   Sr.no              criteria                     amount")
    print("    1.              Person charge -             RS. ",per,"*",num1)
    amt1=per*num1
    if mode=="1a":
            print("    2.              Transport charge            Rs. 1295*",num1)
            amt2=1295*num1
    elif mode=="1b":
            print("    2.              Transport charge            Rs. 2100*",num1)
            amt2=2100*num1
    else:
            print("    2.              Transport charge            Rs. 3000*",num1)
            amt2=3000*num1
    print(" ---------------------------------------------------------------------------------------------\n")
    print("\n   GST:                                    5% of total\n")
    total=amt1+amt2
    gst=total+((5/100)*total)
    print("---------------------------------------------------------------------------------------------")
    print("  SUBTOTAL=                               Rs.",gst)







#function5- updating existing details in databases
def update(x):
    mycur.execute("select * from schemes where mobno={}".format(x))
    data=mycur.fetchall()
    mode1=data[0][3]
    schemeno=data[0][1]
    num=data[0][2]
    while True:
        choice=input("Do you want to change the mode of transport? (yes/no)\n")
        if choice=="yes":
            print("""MODE TO TRANSPORT:

                    1. Railway(rajdhani)
                            a -  3AC train journey
                            b -  2AC train journey

                    2. Via flight\n""")
            mode1=input("Enter desired mode of transport\n")
            if mode1=="1a" or mode1=="1b" or mode1=="2":
                string="update schemes set mode='{}' where mobno={}".format(mode1,x)
                mycur.execute(string)
                c.commit()
                break
            else:
                print("Invalid input.enter again\n")
                continue
        elif choice=="no":
            break
        else:
            continue



    while True:
        choice=input("Do you want to change the number of people travelling? (yes/no)")
        if choice=="yes":
            while True:
                try:
                    num=int(input("Enter number of people travelling\n"))
                    break
                except:
                    print("Invalid input. Enter again\n")
                    continue
            string="UPDATE schemes SET num={} WHERE mobno={}".format(num,x)
            mycur.execute(string)
            c.commit()
            break
        elif choice=="no":
            break
        else:
            continue


    while True:
        choice=input("Do you want to change the scheme (and/or) date of travelling? (yes/no)\n")
        if choice=="yes":
            scheme()
            while True:
                try:
                    schemeno=int(input("Enter number coressponding to scheme you want to select\n"))
                    if schemeno>=1 and schemeno<=4:
                        scheme_no(schemeno)
                        break
                except:
                    print("Invalid input. Enter again\n")
                    continue
            while True:
                date=input("From the given dates in schemes select trip number(corresponding date of travel will be booked)\n")
                if date>='1' and date<='5':
                   break
                else:
                   print("Invalid input. Enter agaian")
                   continue
                break
            string="UPDATE schemes SET date='{}', schemeinfo={} WHERE mobno={}".format(date,schemeno,x)
            mycur.execute(string)
            c.commit()
            break
        elif choice=="no":
            break
        else:
            continue

    print("Your updated bill is as follows-\n")
    bill(schemeno,num,mode1)





#function 6- delete records
def delete(x):
  while True:
    print("""        1. Do you wish to cancel your booking?
    2. Do you wish to deactivate your \"MUSAFIR\" account?
                                        (account deactivation cancels all your booked tours)
    3. Exit""")
    choice=input("Enter your choice (1/2)")
    if choice=="1":
        st="delete from schemes where mobno={}".format(x)
        mycur.execute(st)
        c.commit()
        break
    elif choice=="2":
        st1="delete from schemes where mobno={}".format(x)
        st2="delete from musafirs where mobno={}".format(x)
        mycur.execute(st1)
        c.commit()
        mycur.execute(st2)
        c.commit()
        break
    elif choice=="3":
        break
    else:
        print("Invalid input. Enter again")
        continue






#function 7- display records
def display(x):
    sc=["Himalayan Trek","White Water Rafting","Seven Sisters","Kerala"]
    date=[["2-3-20 to 6-3-20", "15-3-20 to 20-3-20","8-4-20 to 12-4-20","7-5-20 to 11-5-20","26-5-20 to 30-5-30"],
          ["25-3-20 to 28-3-20","02-4-20 to 05-4-20","23-5-20 to 26-5-20","17-6-20 to 20-6-20", "27-6-20 to 30-6-20"],
          ["18-3-20 to 28-3-20","20-4-20 to 12-4-20","16-5-20 to 26-5-20","17-6-20 to 27-6-20","20-6-20 to 30-6-20"],
          ["22-3-20 to 28-3-20","02-4-20 to 08-4-20","24-5-20 to 30-5-20","17-6-20 to 23-6-20","24-6-20 to 30-6-20"]]
    mode={'1a':"3 Tier AC",'1b':"2 Tier AC",'2':"Flight"}

    st="select * from schemes where mobno={}".format(x)
    mycur.execute(st)
    data=mycur.fetchall()
    if mycur.rowcount==0:
        print("You don't have any active trips")
    else:
        p=data[0][1]
        t=int(p)
        schemeinfo=sc[t-1]
        d=data[0][4]
        e=int(d)
        tour=date[t-1][e-1]
        mode1=data[0][3]
        print("mobile no.:         ",data[0][0])
        print("number of people:   ",data[0][2])
        print("tour:               ",schemeinfo)
        print("mode:               ",mode[mode1])
        print("date:               ",tour)




#function 8- function call
def bigfunc(x):
    while True: #1
        choice=input("""                       Select number coressponding to your choice
                        --------------------------------------------

                        1. Book a tour
                        2. Update details for tour
                        3. Delete prebooked tour/account
                        4. View your trip summary
                        5. Exit\n""")

        if choice=="1":
            
            while True:#2
                            scheme()
                            while True:
                                try:
                                     schemeno=int(input("Enter number corresponding to the scheme you want to select\n"))
                                     if schemeno>=1 and schemeno<=4:
                                        scheme_no(schemeno)
                                        break
                                except:
                                     print("Invalid input. Enter again\n")
                                     continue

                            choice2=input("Do you want to join the trip? (yes/no/exit)\n")
                            if choice2=="yes":
                                  print("Please fill in the following form\n")
                                  num,mode=form(schemeno)
                                  print("Thankyou for joing our adventure tour !!\n                        YOUR BILL IS AS FOLLOWS\n")
                                  bill(schemeno,num,mode)
                                  print("                         THANKYOU!!!!")
                                  break
                            elif choice2=="no":
                                continue
                            elif choice2=="exit":
                                break# to come out of 2
                            else:
                                print("Invalid Input. Enter again")
                                continue
                            break# this break is to come out of 1
            continue# this is to re print 1

        elif choice=="2":
            update(x)
            continue
        elif choice=="3":
            delete(x)
            print("Your desired record has been successfully deleted. Press 5 and exit.")
            continue
        elif choice=="4":
            display(x)
            continue
        elif choice=="5":
            break# to come out of loop
        else:
            print("Invalid choice.")
            continue
        break# to terminate program
                
                                
                        


#main function


myfile=open(r"C:\Users\DELL\Desktop\Aarohi\display.txt","r")
string=myfile.read()
print(string)

while True:
 while True:
   try:
        musafir=input("Are you a frequent musafir?(yes/no). If not sign up to avail schemes.\nOr input exit to leave\n")
        if musafir == 'yes' or musafir=='no' or musafir=='exit':
            break
        else:
            continue
   except:
        print("Invalid choice. Enter again.\n")
        continue


 if musafir=='no':
    #registration
    mname=input("Enter your name.\n")
    while True:
        mob=input("Enter 10 digit registered mobile number\n")
        if len(mob)==10:
            mobno=int(mob)
            break
        else:
            print("Invalid mobile number.Enter again.\n")
            continue
    string="INSERT INTO musafirs(mobno,mname) VALUES({},'{}')".format(mobno,mname)
    mycur.execute(string)
    c.commit()

    #scheme display
    print("\n                                      -----------------------------------------------------")
    print("                                        Now you a registered musafir with safarnama tours !!!")
    print("                                        -----------------------------------------------------\n")


    bigfunc(mobno)
    continue


 elif musafir=="yes":
    mycur.execute("select mobno from musafirs;")
    data=mycur.fetchall()
    l=len(data)
    while True:
        mob=input("Enter 10 digit registered mobile number\n")
        if len(mob)==10:
            mobno1=int(mob)
            for i in range(l):
                lst=list(data[i])
                lst2=lst[0]
                if mobno1 == lst2:
                    bigfunc(mobno1)
                    break
                else:
                    continue
            else:
                print("Not a registered musafir. Sign up")
                break
        else:
            print("Invalid input.Enter again")
            break
        break
    continue
 elif musafir=='exit':
     break
 break
        

    
    












        
