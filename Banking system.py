from tkinter import *
from tkinter import messagebox
import smtplib
import datetime
import random

dt=datetime.datetime.now()
date=str(dt)[0:10]
time=str(dt)[11:19]

win = Tk()
win.title("Bank")
win.geometry("1450x906")

balance=''
name=''
n=0
ac=""


def f1():

    global balance
    global name
    global n
    global ac
    f = open('DB.txt','r')
    l = f.readline()
    d = {}
    while l:
        nl = l.split(" ")
        d[nl[0]]=(nl[1],nl[2],nl[3])
        l = f.readline()
    f.close()
    n=int(t1.get())
    ac=t1.get()
    k=[]
    acn=[]
    for x in d.keys():
        acn.append(x)
    if str(n) not in acn:
        messagebox.showwarning(" ", "user doesnt exist")

    else:
        for x, y in d.items():
            if x == str(n):
                k.append(y[0])
                k.append(y[1])
                k.append(y[2])

        name = k[0]
        balance = k[1]
        password = k[2]
        if t2.get() == password:
            interface()

        elif t2.get() != password:
            messagebox.showwarning(" ", "wrong password")


def interface():

    global win1
    win1=Toplevel(win)
    win1.geometry("1450x906")
    win1.title("Welcome to bank")

    sw=Label(win1,image=im1)
    sw.place(x=0,y=0)

    def vb():

        fr1=Frame(win1,bg="#FADA5E")
        fr1.place(x=320,y=200)

        l3=Label(fr1,text="Current balance : "+balance+" ₹",bg="#FADA5E",fg="black",font=("Times New Roman",20))
        l3.grid(row=0,column=0,padx=300,pady=240)

    def dep():

        global balance
        global t3

        fr2 = Frame(win1, bg="#FADA5E")
        fr2.place(x=365, y=200)

        l4=Label(fr2,text="Enter the amount to deposit",bg="#FADA5E",fg="black",font=("Times New Roman",20))
        l4.grid(row=0,column=0,padx=20,pady=240)

        t3=Entry(fr2)
        t3.grid(row=0,column=1,padx=30,pady=240)

        def UB():

            if t3.get().isdigit():
                global balance
                global l5
                global n
                global date
                global time

                fr3 = Frame(win1, bg="#FADA5E")
                fr3.place(x=320, y=200)

                nb = int(balance) + int(t3.get())
                balance = str(nb)

                l5 = Label(fr3, text="Deposit Successful!!", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                l5.grid(row=0, column=0, padx=300, pady=240)

                f=open("DB.txt","r")
                data=f.readlines()
                print(data)
                l=[]
                for z in data:
                    l.append(z.strip().split())
                print(l)

                d={}
                for c in l:
                    d[c[0]]=c[2]
                print(d)

                ob=''
                for v,w in d.items():
                    if v==ac:
                        ob=w
                print(ob)

                for u in l:
                    print(u[0],ac,balance)
                    if u[0]==ac:
                        u[u.index(ob)]=balance
                print(l)

                l1=[]
                for k in l:
                    l1.append(" ".join(k))
                print(l1)

                f.close()

                f=open("DB.txt","w")
                for g in l1:
                    f.write(g+"\n")
                f.close()

                cf=open(ac+".txt","a")
                m1="Deposited ₹ "+t3.get()+" on "+date+" at "+time
                cf.write(m1+"\n")
                cf.close()

            else:
                messagebox.showwarning(" ","Enter Only Numbers")

        b4 = Button(fr2, text="Deposit", command=UB)
        b4.grid(row=0,column=2,padx=40)

    def wd():
        global balance

        fr4=Frame(win1,bg="#FADA5E")
        fr4.place(x=365,y=200)

        l4=Label(fr4,text="Enter the amount to withdraw",bg="#FADA5E",fg="black",font=("Times New Roman",20))
        l4.grid(row=0,column=0,padx=20,pady=240)

        t4=Entry(fr4)
        t4.grid(row=0,column=1,padx=30,pady=240)

        def wdb():
            if t4.get().isdigit():
                global balance
                if int(t4.get())<=int(balance):

                    fr5 = Frame(win1,bg="#FADA5E")
                    fr5.place(x=320, y=200)

                    nb = int(balance) - int(t4.get())
                    balance = str(nb)

                    l6 = Label(fr5, text= "Withdraw successfull",bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l6.grid(row=0,column=0,padx=300,pady=240)

                    f = open("DB.txt", "r")
                    d = f.readlines()
                    print(d)
                    l = []
                    for z in d:
                        l.append(z.strip().split())
                    print(l)

                    d = {}

                    for c in l:
                        d[c[0]] = c[2]
                    print(d)

                    ob = ''
                    for v, w in d.items():
                        if v == ac:
                            ob = w
                    print(ob)

                    for u in l:
                        print(u[0], ac, balance)
                        if u[0] == ac:
                            u[u.index(ob)] = balance
                    print(l)

                    l1 = []
                    for k in l:
                        l1.append(" ".join(k))
                    print(l1)

                    f.close()

                    f = open("DB.txt", "w")
                    for g in l1:
                        f.write(g + "\n")
                    f.close()

                    cf = open(ac + ".txt", "a")
                    m1 = "Withdrew ₹ " + t4.get() + " on " + date + " at " + time
                    cf.write(m1 + "\n")
                    cf.close()

                else:
                    messagebox.showwarning(" "," No enough balance ")

            else:
                messagebox.showwarning(" ","Enter Only Numbers")

        b5 = Button(fr4, text="With Draw", command=wdb)
        b5.grid(row=0,column=2,padx=40,pady=240)

    def Loan():

        fr6=Frame(win1,bg="#FADA5E")
        fr6.place(x=320,y=200)

        def car():

            fr7=Frame(win1,bg="#FADA5E")
            fr7.place(x=370,y=200)

            l11=Label(fr7,text="Enter the loan amount",bg="#FADA5E",fg="black",font=("Times New Roman",20))
            l11.grid(row=2,column=0,padx=40,pady=40)

            t11 = Entry(fr7)
            t11.grid(row=2, column=1,padx=40)

            l14=Label(fr7,image=im8,borderwidth=0,bg="#FADA5E")
            l14.grid(row=5,column=1,pady=80)

            l15=Label(fr7,image=im8,borderwidth=0,bg="#FADA5E")
            l15.grid(row=0,column=0,padx=20,pady=40)

            l16=Label(fr7,text="select period",bg="#FADA5E",fg="black",font=("Times New Roman",20))
            l16.grid(row=2,column=2)

            s=Scale(fr7, from_=1, to=10, orient=HORIZONTAL)
            s.grid(row=1,column=2,padx=40)

            def cl():

                global mail2, name1, La
                if t11.get().isdigit():
                    fr8=Frame(win1,bg="#FADA5E")
                    fr8.place(x=320,y=200)

                    l13=Label(fr8,text="Principle loan amount "+t11.get()+" ₹",bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l13.grid(row=2,column=0,padx=270,pady=20)

                    tip=format(((int(t11.get())*7.9)/100)*s.get(),".2f")

                    l14=Label(fr8,text="Total interest Payable "+str(tip)+" ₹",bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l14.grid(row=3,column=0,padx=100,pady=20)

                    tp=int(t11.get())
                    tp1=tip

                    tp2=float(tp)+float(tp1)

                    l15=Label(fr8,text="Total Amount Payable "+str(tp2)+" ₹",bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l15.grid(row=4,column=0,padx=100,pady=20)

                    emi=format(tp2/(int(s.get())*12),".2f")

                    y=""
                    if s.get()==1:
                        y=" Year"
                    else:
                        y=" Years"

                    l16=Label(fr8,text=str(emi)+' ₹ EMI for '+str(s.get())+y,bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l16.grid(row=5,column=0,padx=100,pady=20)

                    l17=Label(fr8,text="Interest rate 7.9%",bg="#FADA5E",fg="black",font=("Times New Roman",20))
                    l17.grid(row=1,column=0,padx=100,pady=20)

                    l18=Label(fr8,image=im8,borderwidth=0,bg="#FADA5E")
                    l18.grid(row=0,column=0)

                    l19=Label(fr8,image=im8,borderwidth=0,bg="#FADA5E")
                    l19.grid(row=6,column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail2 = y[3]

                    f11=open("Loan.txt","a")
                    mes=ac+" Applied for Car Loan of ₹ "+t11.get()
                    f11.write(mes+"\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail2
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations ,"+name1+" Your Application of Car Loan sent successfully"
                    server1 = smtplib.SMTP("smtp.gmail.com", 587)
                    server1.starttls()
                    server1.login(sender_email, passw)
                    server1.sendmail(sender_email, r, m)
                    server1.quit()

                else:
                    messagebox.showwarning(" ","Enter only numbers")

            b10=Button(fr7,text="submit",command=cl)
            b10.grid(row=4,column=1)

        def bike():
            fr8 = Frame(win1, bg="#FADA5E")
            fr8.place(x=370, y=200)

            l21 = Label(fr8, text="Enter the loan amount", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l21.grid(row=2, column=0, padx=40, pady=40)

            t12 = Entry(fr8)
            t12.grid(row=2, column=1, padx=40)

            l24 = Label(fr8, image=im8, borderwidth=0, bg="#FADA5E")
            l24.grid(row=5, column=1, pady=80)

            l25 = Label(fr8, image=im8, borderwidth=0, bg="#FADA5E")
            l25.grid(row=0, column=0, padx=20, pady=40)

            l26 = Label(fr8, text="select period", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l26.grid(row=2, column=2)

            s1 = Scale(fr8, from_=1, to=10, orient=HORIZONTAL)
            s1.grid(row=1, column=2, padx=40)

            def bl():
                if t12.get().isdigit():
                    fr9 = Frame(win1, bg="#FADA5E")
                    fr9.place(x=320, y=200)

                    l13 = Label(fr9, text="Principle loan amount " + t12.get() + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l13.grid(row=2, column=0, padx=270, pady=20)

                    tip = format(((int(t12.get()) * 6.7) / 100) * s1.get(), ".2f")

                    l14 = Label(fr9, text="Total interest Payable " + str(tip) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l14.grid(row=3, column=0, padx=100, pady=20)

                    tp = int(t12.get())
                    tp1 = tip

                    tp2 = float(tp) + float(tp1)

                    l15 = Label(fr9, text="Total Amount Payable " + str(tp2) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l15.grid(row=4, column=0, padx=100, pady=20)

                    emi = format(tp2 / (int(s1.get()) * 12), ".2f")

                    y = ""
                    if s1.get() == 1:
                        y = " Year"
                    else:
                        y = " Years"

                    l16 = Label(fr9, text=str(emi) + ' ₹ EMI for ' + str(s1.get()) +y, bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l16.grid(row=5, column=0, padx=100, pady=20)

                    l17 = Label(fr9, text="Interest rate 6.7%", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                    l17.grid(row=1, column=0, padx=100, pady=20)

                    l18 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l18.grid(row=0, column=0)

                    l19 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l19.grid(row=6, column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail3 = y[3]

                    f11 = open("Loan.txt", "a")
                    mes = ac + " Applied for Bike Loan of ₹ " + t12.get()
                    f11.write(mes + "\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail3
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations, Your Bike Loan Application sent successfully"
                    m1 = str(m)
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m1)
                    server.quit()

                else:
                    messagebox.showwarning(" ", "Enter only numbers")

            b11 = Button(fr8, text="submit", command=bl)
            b11.grid(row=4, column=1)

        def house():
            fr10 = Frame(win1, bg="#FADA5E")
            fr10.place(x=370, y=200)

            l21 = Label(fr10, text="Enter the loan amount", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l21.grid(row=2, column=0, padx=40, pady=40)

            t12 = Entry(fr10)
            t12.grid(row=2, column=1, padx=40)

            l24 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l24.grid(row=5, column=1, pady=80)

            l25 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l25.grid(row=0, column=0, padx=20, pady=40)

            l26 = Label(fr10, text="select period", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l26.grid(row=2, column=2)

            s1 = Scale(fr10, from_=1, to=10, orient=HORIZONTAL)
            s1.grid(row=1, column=2, padx=40)

            def hl():
                if t12.get().isdigit():
                    fr9 = Frame(win1, bg="#FADA5E")
                    fr9.place(x=320, y=200)

                    l13 = Label(fr9, text="Principle loan amount " + t12.get() + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l13.grid(row=2, column=0, padx=270, pady=20)

                    tip = format(((int(t12.get()) * 6.8) / 100) * s1.get(), ".2f")

                    l14 = Label(fr9, text="Total interest Payable " + str(tip) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l14.grid(row=3, column=0, padx=100, pady=20)

                    tp = int(t12.get())
                    tp1 = tip

                    tp2 = float(tp) + float(tp1)

                    l15 = Label(fr9, text="Total Amount Payable " + str(tp2) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l15.grid(row=4, column=0, padx=100, pady=20)

                    emi = format(tp2 / (int(s1.get()) * 12), ".2f")

                    y = ""
                    if s1.get() == 1:
                        y = " Year"
                    else:
                        y = " Years"

                    l16 = Label(fr9, text=str(emi) + ' ₹ EMI for ' + str(s1.get()) +y, bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l16.grid(row=5, column=0, padx=100, pady=20)

                    l17 = Label(fr9, text="Interest rate 6.8%", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                    l17.grid(row=1, column=0, padx=100, pady=20)

                    l18 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l18.grid(row=0, column=0)

                    l19 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l19.grid(row=6, column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail4 = y[3]

                    f11 = open("Loan.txt", "a")
                    mes = ac + " Applied for Home Loan of ₹ " + t12.get()
                    f11.write(mes + "\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail4
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations, Your Home Loan Application sent successfully"
                    m1 = str(m)
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m1)
                    server.quit()

                else:
                    messagebox.showwarning(" ", "Enter only numbers")

            b11 = Button(fr10, text="submit", command=hl)
            b11.grid(row=4, column=1)

        def agri():
            fr10 = Frame(win1, bg="#FADA5E")
            fr10.place(x=370, y=200)

            l21 = Label(fr10, text="Enter the loan amount", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l21.grid(row=2, column=0, padx=40, pady=40)

            t12 = Entry(fr10)
            t12.grid(row=2, column=1, padx=40)

            l24 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l24.grid(row=5, column=1, pady=80)

            l25 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l25.grid(row=0, column=0, padx=20, pady=40)

            l26 = Label(fr10, text="select period", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l26.grid(row=2, column=2)

            s1 = Scale(fr10, from_=1, to=10, orient=HORIZONTAL)
            s1.grid(row=1, column=2, padx=40)

            def al():
                global mail5
                if t12.get().isdigit():
                    fr9 = Frame(win1, bg="#FADA5E")
                    fr9.place(x=320, y=200)

                    l13 = Label(fr9, text="Principle loan amount " + t12.get() + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l13.grid(row=2, column=0, padx=270, pady=20)

                    tip = format(((int(t12.get()) * 7.25) / 100) * s1.get(), ".2f")

                    l14 = Label(fr9, text="Total interest Payable " + str(tip) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l14.grid(row=3, column=0, padx=100, pady=20)

                    tp = int(t12.get())
                    tp1 = tip

                    tp2 = float(tp) + float(tp1)

                    l15 = Label(fr9, text="Total Amount Payable " + str(tp2) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l15.grid(row=4, column=0, padx=100, pady=20)

                    emi = format(tp2 / (int(s1.get()) * 12), ".2f")

                    y = ""
                    if s1.get() == 1:
                        y = " Year"
                    else:
                        y = " Years"

                    l16 = Label(fr9, text=str(emi) + ' ₹ EMI for ' + str(s1.get()) + y, bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l16.grid(row=5, column=0, padx=100, pady=20)

                    l17 = Label(fr9, text="Interest rate 7.25%", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                    l17.grid(row=1, column=0, padx=100, pady=20)

                    l18 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l18.grid(row=0, column=0)

                    l19 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l19.grid(row=6, column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail5 = y[3]

                    f11 = open("Loan.txt", "a")
                    mes = ac + " Applied for Home Loan of ₹ " + t12.get()
                    f11.write(mes + "\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail5
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations, Your Agricultural Loan Application sent successfully"
                    m1 = str(m)
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m1)
                    server.quit()

                else:
                    messagebox.showwarning(" ", "Enter only numbers")

            b11 = Button(fr10, text="submit", command=al)
            b11.grid(row=4, column=1)

        def edu():
            fr10 = Frame(win1, bg="#FADA5E")
            fr10.place(x=370, y=200)

            l21 = Label(fr10, text="Enter the loan amount", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l21.grid(row=2, column=0, padx=40, pady=40)

            t12 = Entry(fr10)
            t12.grid(row=2, column=1, padx=40)

            l24 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l24.grid(row=5, column=1, pady=80)

            l25 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l25.grid(row=0, column=0, padx=20, pady=40)

            l26 = Label(fr10, text="select period", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l26.grid(row=2, column=2)

            s1 = Scale(fr10, from_=1, to=10, orient=HORIZONTAL)
            s1.grid(row=1, column=2, padx=40)

            def el():
                global mail6
                if t12.get().isdigit():
                    fr9 = Frame(win1, bg="#FADA5E")
                    fr9.place(x=320, y=200)

                    l13 = Label(fr9, text="Principle loan amount " + t12.get() + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l13.grid(row=2, column=0, padx=270, pady=20)

                    tip = format(((int(t12.get()) * 6.85) / 100) * s1.get(), ".2f")

                    l14 = Label(fr9, text="Total interest Payable " + str(tip) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l14.grid(row=3, column=0, padx=100, pady=20)

                    tp = int(t12.get())
                    tp1 = tip

                    tp2 = float(tp) + float(tp1)

                    l15 = Label(fr9, text="Total Amount Payable " + str(tp2) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l15.grid(row=4, column=0, padx=100, pady=20)

                    emi = format(tp2 / (int(s1.get()) * 12), ".2f")

                    y = ""
                    if s1.get() == 1:
                        y = " Year"
                    else:
                        y = " Years"

                    l16 = Label(fr9, text=str(emi) + ' ₹ EMI for ' + str(s1.get()) + y, bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l16.grid(row=5, column=0, padx=100, pady=20)

                    l17 = Label(fr9, text="Interest rate 6.85%", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                    l17.grid(row=1, column=0, padx=100, pady=20)

                    l18 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l18.grid(row=0, column=0)

                    l19 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l19.grid(row=6, column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail6 = y[3]

                    f11 = open("Loan.txt", "a")
                    mes = ac + " Applied for Home Loan of ₹ " + t12.get()
                    f11.write(mes + "\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail6
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations, Your Educational Loan Application sent successfully"
                    m1 = str(m)
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m1)
                    server.quit()

                else:
                    messagebox.showwarning(" ", "Enter only numbers")

            b11 = Button(fr10, text="submit", command=el)
            b11.grid(row=4, column=1)

        def business():

            fr10 = Frame(win1, bg="#FADA5E")
            fr10.place(x=370, y=200)

            l21 = Label(fr10, text="Enter the loan amount", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l21.grid(row=2, column=0, padx=40, pady=40)

            t12 = Entry(fr10)
            t12.grid(row=2, column=1, padx=40)

            l24 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l24.grid(row=5, column=1, pady=80)

            l25 = Label(fr10, image=im8, borderwidth=0, bg="#FADA5E")
            l25.grid(row=0, column=0, padx=20, pady=40)

            l26 = Label(fr10, text="select period", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
            l26.grid(row=2, column=2)

            s1 = Scale(fr10, from_=1, to=10, orient=HORIZONTAL)
            s1.grid(row=1, column=2, padx=40)

            def bul():
                global mail7
                if t12.get().isdigit():
                    fr9 = Frame(win1, bg="#FADA5E")
                    fr9.place(x=320, y=200)

                    l13 = Label(fr9, text="Principle loan amount " + t12.get() + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l13.grid(row=2, column=0, padx=270, pady=20)

                    tip = format(((int(t12.get()) * 9.0) / 100) * s1.get(), ".2f")

                    l14 = Label(fr9, text="Total interest Payable " + str(tip) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l14.grid(row=3, column=0, padx=100, pady=20)

                    tp = int(t12.get())
                    tp1 = tip

                    tp2 = float(tp) + float(tp1)

                    l15 = Label(fr9, text="Total Amount Payable " + str(tp2) + " ₹", bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l15.grid(row=4, column=0, padx=100, pady=20)

                    emi = format(tp2 / (int(s1.get()) * 12), ".2f")

                    y = ""
                    if s1.get() == 1:
                        y = " Year"
                    else:
                        y = " Years"

                    l16 = Label(fr9, text=str(emi) + ' ₹ EMI for ' + str(s1.get()) + y, bg="#FADA5E", fg="black",
                                font=("Times New Roman", 20))
                    l16.grid(row=5, column=0, padx=100, pady=20)

                    l17 = Label(fr9, text="Interest rate 9.0%", bg="#FADA5E", fg="black", font=("Times New Roman", 20))
                    l17.grid(row=1, column=0, padx=100, pady=20)

                    l18 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l18.grid(row=0, column=0)

                    l19 = Label(fr9, image=im8, borderwidth=0, bg="#FADA5E")
                    l19.grid(row=6, column=0)

                    f = open("DB.txt", "r")
                    d = f.readlines()

                    l = []
                    for i in d:
                        l.append(i.strip().split())
                    print(l)

                    d = {}
                    for j in l:
                        d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
                    print(d)
                    f.close()

                    for x, y in d.items():
                        if x == ac:
                            name1 = y[0]
                            mail7 = y[3]

                    f11 = open("Loan.txt", "a")
                    mes = ac + " Applied for Home Loan of ₹ " + t12.get()
                    f11.write(mes + "\n")
                    f11.close()

                    sender_email = "gbubank000@gmail.com"
                    r = mail7
                    passw = "znru rkdm jhwf ewab"
                    m = "Congratulations, Your Business Loan Application sent successfully"
                    m1 = str(m)
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m1)
                    server.quit()

                else:
                    messagebox.showwarning(" ", "Enter only numbers")

            b11 = Button(fr10, text="submit", command=bul)
            b11.grid(row=4, column=1)

        l60=Label(fr6,text="Select  Loan  Type",bg="#FFC000", fg="black", font=("Times New Roman", 30))
        l60.grid(row=0,column=1)

        b10=Button(fr6,image=im2,command=car)
        b10.grid(row=1,column=0,padx=50,pady=40)

        b11=Button(fr6,image=im3,command=bike)
        b11.grid(row=1,column=1,padx=50,pady=40)

        b12=Button(fr6,image=im4,command=house)
        b12.grid(row=1,column=2,padx=50,pady=40)

        b13=Button(fr6,image=im5,command=agri)
        b13.grid(row=2,column=0,padx=50,pady=40)

        b14=Button(fr6,image=im6,command=edu)
        b14.grid(row=2,column=1,padx=50,pady=40)

        b15=Button(fr6,image=im7,command=business)
        b15.grid(row=2,column=2,padx=40,pady=40)

    def vp():

        global n, nl1 , name , balance, ph, email

        name1=name.replace("_"," ")

        f=open("DB.txt","r")
        data=f.readline()
        d1={}
        while data:
            nl1 = data.split(" ")
            d1[nl1[0]] = (nl1[1], nl1[2], nl1[3], nl1[4], nl1[5])
            data = f.readline()

        for x,y in d1.items():
            if x==str(n):
                email=y[3]
                ph=y[4]
        f.close()
        fr10=Frame(win1,bg="#FADA5E")
        fr10.place(x=320,y=200)

        l52=Label(fr10,image=im8,borderwidth=0)
        l52.grid(row=0,column=0,padx=60,pady=20)

        l50=Label(fr10,image=im8,borderwidth=0)
        l50.grid(row=0,column=1,padx=100,pady=25)

        l51=Label(fr10,image=im8,borderwidth=0)
        l51.grid(row=0,column=3,padx=80)

        l30=Label(fr10,text="Name :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l30.grid(row=1,column=1,pady=20)

        l31=Label(fr10,text=name1,bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l31.grid(row=1,column=2)

        l32=Label(fr10,text="Account Number :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l32.grid(row=2,column=1,padx=20,pady=20)

        l33=Label(fr10,text=n,bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l33.grid(row=2,column=2)

        l44=Label(fr10,text="Contact Number :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l44.grid(row=3,column=1,pady=20)

        l45=Label(fr10,text=ph,bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l45.grid(row=3,column=2)

        l46=Label(fr10,text="E-Mail :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l46.grid(row=4,column=1,pady=20)

        l47=Label(fr10,text=email,bg="#FADA5E", fg="black", font=("Times New Roman", 20))
        l47.grid(row=4,column=2)

        l48=Label(fr10,image=im8,borderwidth=0)
        l48.grid(row=5,column=0,pady=40)

    def tr():

        fr30=Frame(win1,bg="#FADA5E")
        fr30.place(x=320,y=200)

        f60=open(ac+".txt","r")
        data2=f60.readlines()
        f60.close()

        l80=Label(fr30,text="Transaction History",font=("Helvetica",20,"bold italic"),bg="#FADA5E",fg="black")
        l80.grid(row=0,column=0)

        if len(data2)!=0:
            listbox=Listbox(fr30,width=70,height=25,bg="#FFC000",fg="black")
            for _ in data2:
                listbox.insert(END,_.strip()+"\n\n\n\n")
            listbox.grid(row=1,column=0,padx=90,pady=10)
        else:
            listbox = Listbox(fr30, width=70, height=25, bg="#FFC000", fg="black")
            listbox.insert(END,"No Transactions are Done")
            listbox.grid(row=1, column=0, padx=90, pady=10)

    def cr():

        f200=open("Cr.txt","r")
        data5=f200.readlines()
        f200.close()

        listcr=[]
        for l in data5:
            listcr.append(l.split())

        print(listcr)

        if [ac] in listcr:

            fr35 = Frame(win1, bg="#FADA5E")
            fr35.place(x=320, y=200)

            l200=Label(fr35,image=creditim)
            l200.grid(row=0,column=0,padx=150,pady=70)

            l201=Label(win1,text="A/C Holder : "+name.replace("_"," "),bg="black",fg="#FFC000")
            l201.place(x=580,y=510)

            l202=Label(win1,text="G.B.U BANK",font=("Arial",20),bg="black",fg="#FFE433",pady=11)
            l202.place(x=680,y=340)

            l205=Label(win1,image=crim,borderwidth=0)
            l205.place(x=630,y=340)

            CRl = []
            for j in range(10):
                CRl.append(str(j))

            Crnum = ""
            for i in range(16):
                temp6 = 0
                if i in [3, 7, 11]:
                    temp6 = 1
                Crnum = Crnum + random.choice(CRl) + "     " * temp6

            l203=Label(win1,text=Crnum,font=("Arial",18),bg="black",fg="#FFC000")
            l203.place(x=650,y=420)

            l204=Label(win1,text="Valid Till :"+" 02/52",bg="black",fg="#FFC000")
            l204.place(x=770,y=510)


    l70=Label(win1,text="WELCOME !!",font=("Helvetica",30,"bold italic"),width=40,height=10,bg="#FFC000",fg="black")
    l70.place(x=380,y=270)

    b2=Button(win1,image=im10,command=vb)
    b2.place(x=70,y=188)

    b3=Button(win1,image=im11,command=dep)
    b3.place(x=70,y=328)

    b4=Button(win1,image=im12,command=wd)
    b4.place(x=70,y=473)

    b5=Button(win1,image=im13,command=Loan)
    b5.place(x=70,y=616)

    b6=Button(win1,image=im14,command=vp)
    b6.place(x=1215,y=188)

    b7=Button(win1,image=im15,command=tr)
    b7.place(x=1215,y=328)

    b8=Button(win1,image=crb,command=cr)
    b8.place(x=1215,y=473)

    b9=Button(win1,image=im16,command=quit)
    b9.place(x=1215,y=616)


def register():

    win2=Toplevel(win)
    win2.title("Registration")
    win2.geometry("1450x906")

    rw=Label(win2,image=im1)
    rw.place(x=0,y=0)

    l6=Label(win2,text="Name",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
    t6=Entry(win2)

    l7=Label(win2,text="Contact number",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
    t7=Entry(win2)

    l8=Label(win2,text="E-mail",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
    t8=Entry(win2)

    l9=Label(win2,text="Set Password",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
    t9=Entry(win2,show="*")

    l10=Label(win2,text="Confirm Password",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
    t10=Entry(win2,show="*")

    def sub():

        n=t6.get()
        Cn=t7.get()
        mail=t8.get()
        pas=t9.get()
        cpas=t10.get()

        if Cn.isdigit():
            if len(pas)>=8:
                temp1 = 0
                temp2 = 0
                temp3 = 0
                temp4 = 0
                for i in pas:
                    if i.isdigit():
                        temp1 = temp1 + 1
                    elif i.islower():
                        temp2 = temp2 + 1
                    elif i.isupper():
                        temp3 = temp3 + 1
                    elif i.isascii():
                        temp4 = temp4 + 1
                if temp1!=0 and temp2!=0 and temp3!=0 and temp4!=0:
                    fil = open('DB.txt', 'a')
                    if pas==cpas and len(pas)!=0 and len(cpas)!=0 :
                        if (mail[-10:-1:1]+"m")=="@gmail.com":
                            fil1=open("DB.txt","r")
                            data=fil1.readlines()
                            last = data[len(data) - 1].split(' ')
                            na=str(int(last[0]) + 1)
                            fil1.close()

                            n1=n.replace(" ","_")
                            fil.write("\n"+na+" "+n1+" "+"0"+" "+pas+" "+mail+" "+Cn)
                            fil.close()

                            rs = Label(win2, image=im1)
                            rs.place(x=0, y=0)

                            l11 = Label(win2, text="Registration Successful!!", bg="#FADA5E", fg="black",
                                        font=("Times New Roman", 20),
                                        padx=50)
                            l11.place(x=550, y=400)

                            sender_email = "gbubank000@gmail.com"
                            r = mail
                            passw = "znru rkdm jhwf ewab"
                            m = "Welcome to G.B.U Bank \nYour account number : " + na + "\nPassoword : " + pas + "\n\n\nThankYou for choosing our bank "

                            server = smtplib.SMTP("smtp.gmail.com", 587)
                            server.starttls()
                            server.login(sender_email, passw)
                            server.sendmail(sender_email, r, m)
                            server.quit()

                            f100=open(na+".txt","a")
                            f100.write("")
                            f100.close()

                            f20=open("Cr.txt","a")
                            f20.write("\n"+na+"\n")
                            f20.close()

                        else:
                            messagebox.showwarning(" ","Invalid E-Mail")

                    else:
                        messagebox.showwarning(" ", "confirmed password is not matching with password ")

                else:
                    messagebox.showwarning(" ","Password Should Contain lower case, upper case, number and special Character")
            else:
                messagebox.showwarning(" ","The length password should be atleast 8")
        else:
            messagebox.showwarning(" ","Invalid Contact Number")

    b6=Button(win2,text="Submit",command=sub)

    l6.place(x=500,y=300)
    t6.place(x=650,y=300)

    l7.place(x=500,y=350)
    t7.place(x=650,y=350)

    l8.place(x=500, y=400)
    t8.place(x=650, y=400)

    l9.place(x=500, y=450)
    t9.place(x=650, y=450)

    l10.place(x=500, y=500)
    t10.place(x=650, y=500)

    b6.place(x=575, y=600)


def fg():

    win3=Toplevel(win)
    win3.title("Forgot Password")
    win3.geometry("1450x906")

    l70=Label(win3,image=im1)
    l70.place(x=0,y=0)

    l80=Label(win3,text="Account Number :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
    l80.place(x=500,y=300)

    t80=Entry(win3)
    t80.place(x=750,y=300)

    l81=Label(win3,text="Registered E-Mail i.d :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
    l81.place(x=500,y=350)

    t81=Entry(win3)
    t81.place(x=750,y=350)

    l82=Label(win3,text="Registered Mobile number :",bg="#FADA5E", fg="black", font=("Times New Roman", 20))
    l82.place(x=500, y=400)

    t82=Entry(win3)
    t82.place(x=750, y=400)

    def fg1():

        global mail1, ph1, name1 , passw1
        Ac=t80.get()
        Re=t81.get()
        Rm=t82.get()

        f = open("DB.txt", "r")
        d = f.readlines()

        l = []
        for i in d:
            l.append(i.strip().split())
        print(l)

        d = {}
        Acl=[]
        for j in l:
            Acl.append(j[0])
            d[j[0]] = [j[1], j[2], j[3], j[4], j[5]]
        print(d)
        f.close()

        if Ac in Acl:
            for x,y in d.items():
                if x==Ac:
                    name1=y[0]
                    passw1=y[2]
                    mail1=y[3]
                    ph1=y[4]

            if Re==mail1:

                if Rm==ph1:

                    sender_email = "gbubank000@gmail.com"
                    r = mail1
                    passw = "znru rkdm jhwf ewab"
                    m = "Hello "+name1.replace("_"," ")+" ,"+"\n\nYour Account Number : " +Ac+"\nPassword : "+passw1+"\n\n\nThank You"
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, passw)
                    server.sendmail(sender_email, r, m)
                    server.quit()

                    l85=Label(win3,text="Your Account Number and Password has been sent to your e-mail",width=70,height=20,bg="#FADA5E",fg="black",font=("Times New Roman", 20))
                    l85.place(x=350, y=200)

                else:
                    messagebox.showwarning(" ","Mobile Number Does Not Exist")

            else:
                messagebox.showwarning(" ","E-Mail Does not Exist")

        else:
            messagebox.showwarning(" ","Entered Account Number Does Not Exist")

    b40=Button(win3,text="Verify",command=fg1)
    b40.place(x=650,y=500)

    win3.mainloop()


p=PhotoImage(file="3E7B2939-7B06-45F8-AF63-2F00B99F763B.png")
im1=PhotoImage(file="F4AE9F6D-9F52-489D-A436-97848CEE58E9.png")
im2=PhotoImage(file="26FFE7D6-7682-43B9-B683-A126A6B3685D_4_5005_c.png")
im3=PhotoImage(file="6B622319-E545-4D80-8F14-9B5C72D8889C_4_5005_c.png")
im4=PhotoImage(file="D8BA8695-B250-4D9F-B17E-865266EF36ED_4_5005_c.png")
im5=PhotoImage(file="1031273D-1850-47CB-A400-0697A39187B0_4_5005_c.png")
im6=PhotoImage(file="1BD75579-0FAD-46CB-BD33-517DFE5D4B6A_4_5005_c.png")
im7=PhotoImage(file="830AA9F6-41C9-4270-8640-A557C8EC62DF_4_5005_c.png")
im8=PhotoImage(file="05FDB31D-FD49-4378-AEFE-7233AA165227_4_5005_c.png")

im10=PhotoImage(file="vb1.png")
im11=PhotoImage(file="dp.png")
im12=PhotoImage(file="wd.png")
im13=PhotoImage(file="l.png")
im14=PhotoImage(file="pr.png")
im15=PhotoImage(file="tr.png")
im16=PhotoImage(file="8469EADE-B957-4D69-BFFA-828851B17027.png")

creditim=PhotoImage(file="credit.png")
crim=PhotoImage(file="20220129_230128_0000-2.png")

crb=PhotoImage(file="AE1675A4-C328-4C50-9F11-8ABA2AC4D463.png")

mw=Label(win,image=p)
mw.place(x=0,y=0)

l1 = Label(win, text="Enter Account number",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
t1 = Entry(win)

l2 = Label(win, text="Enter Password",bg="#FADA5E", fg="black", font=("Times New Roman", 15))
t2 = Entry(win,show="*")

b1 = Button(win, text=" login", command=f1)

b5 = Button(win,text="Register",command=register)

b6 = Button(win,text="Forgot Password",command=fg)
b6.place(x=1060,y=500)

l1.place(x=830, y=353)
t1.place(x=1000, y=350)

l2.place(x=830, y=403)
t2.place(x=1000, y=400)

b1.place(x=850, y=500)

b5.place(x=950, y=500)

win.mainloop()
