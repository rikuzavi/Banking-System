import sqlite3
import datetime
import random
import tkinter as T
import smtplib
import webbrowser

Admin_name='patrick bateman'
Admin_pass='phsyco'

D=datetime.date.today()
H=datetime.datetime.now().hour
M=datetime.datetime.now().minute

win = T.Tk()
win.geometry("800x500")
win.title("BOP")
win.configure(bg="grey15")

photo = None


def create_image(x):
    original_image = T.PhotoImage(file="bank.png")  # Replace with your image file path
    resized_image = original_image.subsample(2)
    image_label = T.Label(x, image=resized_image, bg="grey15")
    image_label.image = resized_image
    image_label.place(x=60, y=100)
    l = T.Label(x, text="BANK OF PEOPLE", font=('Rockwell Extra Bold', 25), fg="red3", bg="grey15")
    l.place(x=22, y=420)

def show_dbonline():
    url = 'https://sqliteonline.com/'
    webbrowser.open_new_tab(url)

def acc_balance():
    win3 = T.Toplevel()
    win3.geometry("800x500")
    win3.title("BOP")
    win3.configure(bg="grey15")
    create_image(win3)
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(f"select name,amount from account where accno = {ACNO}")
    record = cur.fetchall()
    R = 'ACCOUNT DETAIL'+'\n\n'
    for item in record:
        for element in item:
            R +="\n"+str(element)

    cur.execute(f"select tran_his from account where accno = {ACNO}")
    record = cur.fetchall()
    his=''
    for item in record[0]:
        his += str(item)
    l5 = T.Label(win3, text=R+" $\n\nTansaction History :\n\n"+his, fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l5.place(x=450, y=80)
    b10 = T.Button(win3, text='M A I N   P A G E    ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),command=win3.destroy)
    b10.place(x=450, y=320)


def deposit():
    win4 = T.Toplevel()
    win4.geometry("800x500")
    win4.title("BOP")
    win4.configure(bg="grey15")
    create_image(win4)
    l5 = T.Label(win4, text="ENTER AMOUNT TO DEPOSIT", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l5.place(x=450, y=110)
    amount = T.Entry(win4, width=25, font=20)
    amount.place(x=450, y=140)
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(f"select amount from account where accno = {ACNO}")
    AMT = cur.fetchall()

    def dep():
        s = ''
        entry_amt = amount.get()
        if (entry_amt == '' or str(entry_amt).isalpha()):
            s += "Invalid Amount"
        elif(int(entry_amt) < 0):
            s += "Invalid Amount"
        else:
            A = ''
            for amt in AMT[0]:
                A += str(amt)
            new_amt = int(A) + int(entry_amt)
            h = f"Credited $ {entry_amt}\ndate : {D}\nTime : {H}:{M}"
            cur.execute(f"update account set amount = {new_amt},tran_his = '{h}' where accno={ACNO}")
            conn.commit()
            s += f"$ {entry_amt} Credited to Account\n\nTotal Balance : $ {new_amt}"
            l5.destroy()
            amount.destroy()
            b11.destroy()
        l6 = T.Label(win4, text=s, fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
        l6.place(x=450, y=330)

    b11 = T.Button(win4, text='D E P O S I T        ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=dep)
    b11.place(x=450, y=200)
    b12 = T.Button(win4, text='M A I N   P A G E    ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                   command=win4.destroy)
    b12.place(x=450, y=240)
    win4.update()


def withdraw():
    win5 = T.Toplevel()
    win5.geometry("800x500")
    win5.title("BOP")
    win5.configure(bg="grey15")
    create_image(win5)
    l7 = T.Label(win5, text="ENTER AMOUNT TO WITHDRAW", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l7.place(x=450, y=110)
    amount = T.Entry(win5, width=25, font=20)
    amount.place(x=450, y=140)
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(f"select amount from account where accno = {ACNO}")
    AMT = cur.fetchall()

    def withd():
        s = ''
        entry_amt = amount.get()
        A = ''
        for amt in AMT[0]:
            A += str(amt)
        if (entry_amt == '' or str(entry_amt).isalpha()):
            s += "Invalid Amount     "
        elif(int(entry_amt) < 0):
            s += "Invalid Amount     "
        elif (int(entry_amt) > int(A)):
            s += "Insufficient Amount"
        else:
            h=f"Debited $ {entry_amt}\ndate : {D}\nTime : {H}:{M}"
            new_amt = int(A) - int(entry_amt)
            cur.execute(f"update account set amount = {new_amt},tran_his = '{h}' where accno={ACNO}")
            conn.commit()
            s += f"$ {entry_amt} Debited from Account\n\nTotal Balance : $ {new_amt}"
            l7.destroy()
            amount.destroy()
            b11.destroy()
        l6 = T.Label(win5, text=s, fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
        l6.place(x=450, y=330)

    b11 = T.Button(win5, text='W I T H D R A W      ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=withd)
    b11.place(x=450, y=200)
    b12 = T.Button(win5, text='M A I N   P A G E    ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                   command=win5.destroy)
    b12.place(x=450, y=240)
    win5.update()


def delete():
    win6 = T.Toplevel()
    win6.geometry("800x500")
    win6.title("BOP")
    win6.configure(bg="grey15")
    create_image(win6)
    l7 = T.Label(win6, text="ENTER PASSWORD", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l7.place(x=450, y=110)
    pas = T.Entry(win6, width=25, font=20)
    pas.place(x=450, y=140)
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(f"select amount from account where accno = {ACNO}")
    AMT = cur.fetchall()
    A = ''
    for amt in AMT[0]:
        A += str(amt)

    cur.execute(f"select pass from account where accno = {ACNO}")
    PAS = cur.fetchall()
    P = ''
    for p in PAS[0]:
        P += p

    def dele():
        s = ''
        passs = pas.get()
        if (passs == ''):
            s += "Invalid Password"
        elif (passs != str(P)):
            s += "* * * Wrong Password * * *"
        elif (int(A) > 0 ):
            s += "! ! ! Bank account contain Amount\nwithdraw before deleting\n$ " + str(A)
        else:
            cur.execute(f"delete from account where accno = {ACNO}")
            conn.commit()
            s += "!  Account Deleted from Database"
        l9 = T.Label(win6, text=s, fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
        l9.place(x=450, y=330)
        win6.update()
    b11 = T.Button(win6, text='D E L E T E   A C C   ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=dele)
    b11.place(x=450, y=200)
    b12 = T.Button(win6, text='M A I N   P A G E     ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                   command=win6.destroy)
    b12.place(x=450, y=240)


def update():
    win7 = T.Toplevel()
    win7.geometry("800x500")
    win7.title("BOP")
    win7.configure(bg="grey15")
    create_image(win7)
    l7 = T.Label(win7, text="UPDATE NAME", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l7.place(x=450, y=110)
    n = T.Entry(win7, width=25, font=20)
    n.place(x=450, y=140)
    l8 = T.Label(win7, text="UPDATE PASSWORD", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l8.place(x=450, y=170)
    password = T.Entry(win7, width=25, font=20)
    password.place(x=450, y=200)
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()

    def upda():
        SUBJECT = 'BANK OF PEOPLE\n Personal info not to be shared'
        em_conf=''
        name = n.get()
        passs = password.get()
        s=''
        if(name=='' or passs==''):
            s+="Entry fields Required"
        else:
            l7.destroy()
            l8.destroy()
            n.destroy()
            password.destroy()
            b11.destroy()
            cur.execute(f"select email from account where accno = {ACNO}")
            record = cur.fetchall()
            mail = ''
            for item in record[0]:
                mail += str(item)
            mes = f"Updation done by you on your BOP Account\n NAME : {name}\n PASSWORD {passs}\nConfidential donot share"
            try:
                sms = smtplib.SMTP('smtp.gmail.com', 587)
                sms.starttls()
                sms.login(user="bankofpeoplebop@gmail.com", password="byoofebjsppicrrd")
                messege = "Subject: {}\n\n acc detail is  {}".format(SUBJECT, mes)
                sms.sendmail(from_addr="bankofpeoplebop@gmail.com", to_addrs=mail, msg=messege)
                sms.close()
                em_conf += 'Email has been sent to your mail id'
            except:
                em_conf += '\nNetwork error\nOR\nEmail not provided'
            finally:
                cur.execute(f"update account set name = '{name}',pass = '{passs}' where accno={ACNO}")
                conn.commit()
            s+=f"Updation Successful\nName : {name}\nPassword : {passs}\nfor Account number : {ACNO}\n{em_conf}"
        l9 = T.Label(win7, text=s, fg="red3",bg="grey15", font=("Rockwell Extra Bold", 13))
        l9.place(x=450, y=330)
        win7.update()

    b11 = T.Button(win7, text='U P D A T E          ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=upda)
    b11.place(x=450, y=230)
    b12 = T.Button(win7, text='M A I N   P A G E    ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),command=win7.destroy)
    b12.place(x=450, y=270)


def create_account():
    win8 = T.Toplevel()
    win8.geometry("800x500")
    win8.title("BOP")
    win8.configure(bg="grey15")
    create_image(win8)
    l7 = T.Label(win8, text="NAME", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l7.place(x=450, y=20)
    l8 = T.Label(win8, text="PASSWORD", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l8.place(x=450, y=80)
    l9 = T.Label(win8, text="EMAIL ID", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l9.place(x=450, y=140)
    n = T.Entry(win8, width=25, font=20)
    n.place(x=450, y=50)
    p = T.Entry(win8, width=25, font=20)
    p.place(x=450, y=110)
    em = T.Entry(win8, width=25, font=20)
    em.place(x=450, y=170)


    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()

    def crea():
        SUBJECT='BANK OF PEOPLE\n Personal info not to be shared'
        no = random.randint(111111, 999999)
        year = datetime.date.today().year
        accno = str(no) + str(year)
        name=n.get()
        pas=p.get()
        email=em.get()
        s=''
        em_conf=''

        if(name!='' and pas!=''):
            l7.destroy()
            l8.destroy()
            l9.destroy()
            n.destroy()
            p.destroy()
            em.destroy()
            b11.destroy()
            mes=f"name : {name}\nAcc no : {accno}\nPassword : {pas}\nBalance : {0}"
            try:
                sms = smtplib.SMTP('smtp.gmail.com', 587)
                sms.starttls()
                sms.login(user="bankofpeoplebop@gmail.com", password="byoofebjsppicrrd")
                messege = "Subject: {}\n\n acc detail is  {}".format(SUBJECT, mes)
                sms.sendmail(from_addr="bankofpeoplebop@gmail.com", to_addrs=email, msg=messege)
                sms.close()
                em_conf+='Email has been sent to your mail id'
            except:
                em_conf+='\nNetwork error\nOR\nEmail not provided'
            finally:
                cur.execute("insert into account values (:accno, :n, :p, :amt,:email, :his)",
                                {
                                    'accno': str(accno),
                                    'n': str(name).upper(),
                                    'p': str(pas),
                                    'amt': '0',
                                    'email': str(email),
                                    'his': ''
                                })
                conn.commit()
            s += f'Bank Account Created\nName : {name}\nAcc No : {accno}\nPass : {pas}\nBalance : $ 0\n{em_conf}'
        else:
            s += 'Entry fields Mandatory Except Email\nOR\nInvalid Entry '
        win8.update()
        l10 = T.Label(win8, text=str(s), fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
        l10.place(x=450, y=300)

    b11 = T.Button(win8, text='C R E A T E            ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=crea)
    b11.place(x=450, y=200)
    b12 = T.Button(win8, text='M A I N   P A G E      ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),command=win8.destroy)
    b12.place(x=450, y=240)



def admin():
    win9 = T.Toplevel()
    win9.geometry("800x500")
    win9.title("BOP")
    win9.configure(bg="grey15")
    l7 = T.Label(win9, text="ID", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 12))
    l7.place(x=10, y=1)
    l8 = T.Label(win9, text="PASSWORD", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 12))
    l8.place(x=250, y=1)
    idd = T.Entry(win9, width=20, font=20)
    idd.place(x=10, y=25)
    p = T.Entry(win9, width=20, font=20)
    p.place(x=250, y=25)

    def show():
        s=''
        id=idd.get()
        pas=p.get()
        if(str(id)!='' and str(pas)!='' and str(id)==Admin_name and str(pas)==Admin_pass):
            idd.destroy()
            p.destroy()
            b11.destroy()
            l7.destroy()
            l8.destroy()

            def search():
                win10 = T.Toplevel()
                win10.geometry("800x500")
                win10.title("BOP")
                win10.configure(bg="grey15")
                idd = T.Entry(win10, width=30, font=25)
                idd.place(x=300, y=20)
                conn = sqlite3.connect('bank.db')
                cur = conn.cursor()

                def detail():
                    R = '' + '\n\n'
                    holder = idd.get()
                    name = str(holder).upper()
                    cur.execute(f"select * from account where accno = '{holder}' or name = '{name}'")
                    record = cur.fetchall()
                    if (record == ''):
                        R += 'NO ACCOUNT AVAILABLE'
                    else:
                        for item in record:
                            for element in item:
                                R += "\n" + str(element)
                        R += '\n\n\n\n\n\n\n\n'
                    l10 = T.Label(win10, text=str(R), fg="red3", bg="grey15", font=("Rockwell Extra Bold", 15))
                    l10.place(x=300, y=120)

                b13 = T.Button(win10, text='F I N D   A C C  ', bg="red3", fg="white", font=("Rockwell Extra Bold", 9),command=detail)
                b13.place(x=300, y=50)

                b15 = T.Button(win10, text='M A I N   P A G E', bg="red3", fg="white", font=("Rockwell Extra Bold", 9),command=win10.destroy)
                b15.place(x=300, y=90)

            b14 = T.Button(win9, text='S H O W   D A T A B A S E ', bg="red3", fg="white",font=("Rockwell Extra Bold", 9), command=show_dbonline)
            b14.place(x=100, y=22)
            b13 = T.Button(win9, text='S E A R C H', bg="red3", fg="white", font=("Rockwell Extra Bold", 9),command=search)
            b13.place(x=400, y=22)
            s+="ACCESS   GRANTED\n\nAdmin have access to database"
        else:
            s+="ACCESS   DENIED\n\ninvalid Or Wrong Id and pass."
        l10 = T.Label(win9, text=str(s), fg="red3", bg="grey15", font=("Rockwell Extra Bold", 15))
        l10.place(x=0, y=90)




    b11 = T.Button(win9, text='L O G   I N', bg="red3", fg="white", font=("Rockwell Extra Bold", 9), command=show)
    b11.place(x=490, y=22)
    b12 = T.Button(win9, text='M A I N   P A G E', bg="red3", fg="white", font=("Rockwell Extra Bold", 9), command=win9.destroy)
    b12.place(x=575, y=22)


def login():
    win1 = T.Toplevel()
    win1.geometry("800x500")
    win1.title("BOP")
    win1.configure(bg="grey15")
    create_image(win1)
    l1 = T.Label(win1, text="ACCOUNT NUMBER  ", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l1.place(x=450, y=110)
    acc_no = T.Entry(win1, width=25, font=20)
    acc_no.place(x=450, y=140)
    l2 = T.Label(win1, text="PASSWORD  ", fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
    l2.place(x=450, y=170)
    pas = T.Entry(win1, width=25, font=20, show='X')
    pas.place(x=450, y=200)

    def submit():
        global ACNO
        dis_text = ""
        ACNO = acc_no.get()
        PASS = pas.get()
        if (ACNO == "" and PASS == ""):
            pass
        elif (ACNO != "" and PASS == ""):
            dis_text += "Password required               \n                                "
        elif (ACNO == "" and PASS != ""):
            dis_text += "Account no. required             \n                                 "
        else:
            conn = sqlite3.connect('bank.db')
            cur = conn.cursor()
            cur.execute(f"select accno from account where accno = '{ACNO}'")
            acountno = cur.fetchall()
            A = ''
            if (acountno == []):
                dis_text += "Invalid Account number\nAccount number doesn't exist"
            else:
                cur.execute(f"select pass from account where accno = {ACNO}")
                accountpass = cur.fetchall()
                P = ''
                for i in accountpass[0]:
                    P += str(i)
                for j in acountno[0]:
                    A += str(j)
                if (P != PASS):
                    dis_text += "Wrong Password                \n                           "
                else:
                    dis_text += ''
                    win1.destroy()
                    win2 = T.Toplevel()
                    win2.geometry("800x500")
                    win2.title("BOP")
                    win2.configure(bg="grey15")
                    create_image(win2)
                    b6 = T.Button(win2, text='A C C   B A L A N C E     ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                  command=acc_balance)
                    b6.place(x=450, y=120)
                    b7 = T.Button(win2, text='D E P O S I T             ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                  command=deposit)
                    b7.place(x=450, y=170)
                    b8 = T.Button(win2, text='W I T H D R A W           ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                  command=withdraw)
                    b8.place(x=450, y=220)
                    b9 = T.Button(win2, text='D E L E T E   A C C       ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                  command=delete)
                    b9.place(x=450, y=270)
                    b11 = T.Button(win2, text='U P D A T E   A C C      ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                   command=update)
                    b11.place(x=450, y=320)
                    b10 = T.Button(win2, text='M A I N   P A G E    ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12),
                                   command=win2.destroy)
                    b10.place(x=450, y=370)
                win1.update()
        l3 = T.Label(win1, text=dis_text, fg="red3", bg="grey15", font=("Rockwell Extra Bold", 13))
        l3.place(x=450, y=350)

    b4 = T.Button(win1, text='S U B M I T        ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=submit)
    b4.place(x=450, y=250)
    b5 = T.Button(win1, text='M A I N   P A G E  ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=win1.destroy)
    b5.place(x=450, y=290)


b1 = T.Button(win, text='L O G   I N                   ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=login)
b1.place(x=450, y=120)
b2 = T.Button(win, text='C R E A T E   A C C O U N T ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=create_account)
b2.place(x=450, y=180)
b3 = T.Button(win, text='A D M I N                   ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=admin)
b3.place(x=450, y=240)
b6 = T.Button(win, text='E X I T                     ', bg="red3", fg="white", font=("Rockwell Extra Bold", 12), command=exit)
b6.place(x=450, y=300)
create_image(win)

win.mainloop()