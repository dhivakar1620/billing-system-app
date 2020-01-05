from tkinter import*
import random
import time
import datetime

sf = open("pgs.txt","a+")

#monitor resolution
width = 1350
height = 750

root = Tk()
root.geometry(str(width)+"x" + str(height) + "+0+0")
root.title("PGS Billing Systems")

Tops = Frame(root, width=width, height=100, bd=8,relief='raise')
Tops.pack(side=TOP)

PaymentRef=StringVar()
x=random.randint(10034,699812)
randomRef=str(x)
PaymentRef.set("BILL"+randomRef)
od=("BILL"+randomRef)
lblRef = Label(Tops,font=('arial',10,'bold'),text='Order ID',bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(Tops,font=('arial',10,'bold'),textvariable=PaymentRef,bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)

na=StringVar()
lblna= Label(Tops,font=('arial',10,'bold'),text='Customer Name',bd=16,justify='left')
lblna.grid(row=1,column=0)
txtna=Entry(Tops,font=('arial',10,'bold'),textvariable=na,bd=10,insertwidth=2,justify='left')
txtna.grid(row=1,column=1)
inp=str(na.get())
sf.write("\nhvhv"+str(inp))



DateofOrder=StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))
da=(time.strftime("%d/%m/%y"))
lblDateofOrder = Label(Tops,font=('arial',10,'bold'),text='Order Date',bd=10,anchor='w')
lblDateofOrder.grid(row=0,column=4)
txtDateofOrder=Entry(Tops,font=('arial',10,'bold'),textvariable=DateofOrder,bd=10,insertwidth=2,justify='left')
txtDateofOrder.grid(row=0,column=5)

#main-frame
f1 = Frame(root, width=900, height=700, bd=8,relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=450, height=700, bd=8,relief='raise')
f2.pack(side=LEFT)
#sub-frame
f1a = Frame(f1, width=900, height=380, bd=8,relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8,relief='raise')
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=450, height=380, bd=8,relief='raise')
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=450, height=380, bd=8,relief='raise')
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=500, height=320, bd=8,relief='raise')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=500, height=320, bd=8,relief='raise')
f2ab.pack(side=LEFT)

lblInfo=Label(Tops,fg='red', font=('arial',50,'bold'),text ="  PGS Billing systems  ", bd=10,anchor='w')
lblInfo.grid(row=0,column=3)

#============
# CALCULATOR
#============

#calculator's screen
text_Input=StringVar()
operator=""

def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

def btnClearDisplay():
        global operator
        operator=''
        text_Input.set('')

def btnEqualsInput():
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator=''

#calculator's buttons
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input,bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
#----------------------------------------------------
btn7 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=1,column=2)
btnPlus = Button(f2,padx=16,pady=16,bd=8,fg='blue',font=('arial',17,'bold'),text='+',command=lambda:btnClick("+")).grid(row=1,column=3)
#----------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=2,column=2)
btnSub = Button(f2,padx=16,pady=16,bd=8,fg='blue',font=('arial',20,'bold'),text='-',command=lambda:btnClick("-")).grid(row=2,column=3)
#----------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=3,column=2)
btnMult = Button(f2,padx=16,pady=16,bd=8,fg='blue',font=('arial',20,'bold'),text='*',command=lambda:btnClick("*")).grid(row=3,column=3)
#----------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear = Button(f2,padx=16,pady=16,bd=8,fg='red',font=('arial',20,'bold'),text='c',command=btnClearDisplay).grid(row=4,column=1)
btnEqual = Button(f2,padx=16,pady=16,bd=8,fg='blue',font=('arial',20,'bold'),text='=',command=btnEqualsInput).grid(row=4,column=2)
btnDiv = Button(f2,padx=16,pady=16,bd=8,fg='blue',font=('arial',20,'bold'),text='/',command=lambda:btnClick("/")).grid(row=4,column=3)


# ORDER's INFO


hb8=StringVar()
hb6=StringVar()
sb8=StringVar()
sb6=StringVar()
sb4=StringVar()
pbz8=StringVar()
pbz6=StringVar()
pbi8=StringVar()
pbi6=StringVar()


hb8.set(0)
hb6.set(0)
sb8.set(0)
sb6.set(0)
sb4.set(0)
pbz8.set(0)
pbz6.set(0)
pbi8.set(0)
pbi6.set(0)


lblhb = Label(f1aa,font=('arial',10,'bold'),text='Hollow Blocks',bd=16,justify='left')
lblhb.grid(row=1,column=0)
lblhb8 = Label(f1aa,font=('arial',10,'bold'),text='8 inch',bd=16,justify='left')
lblhb8.grid(row=0,column=1)
txthb8=Entry(f1aa,font=('arial',8,'bold'),textvariable=hb8,bd=10,insertwidth=2,justify='left')
txthb8.grid(row=1,column=1)
lblhb6 = Label(f1aa,font=('arial',10,'bold'),text='6 inch',bd=16,justify='left')
lblhb6.grid(row=0,column=2)
txthb6=Entry(f1aa,font=('arial',8,'bold'),textvariable=hb6,bd=10,insertwidth=2,justify='left')
txthb6.grid(row=1,column=2)
lblhb = Label(f1aa,fg='red',font=('arial',13,'bold'),text='SKDD pvt.LTD.',bd=16,justify='left')
lblhb.grid(row=1,column=4)

lblsb = Label(f1aa,font=('arial',10,'bold'),text='Solid Blocks',bd=16,justify='left')
lblsb.grid(row=3,column=0)
lblsb = Label(f1aa,font=('arial',10,'bold'),text='8 inch',bd=16,justify='left')
lblsb.grid(row=2,column=1)
txtsb=Entry(f1aa,font=('arial',8,'bold'),textvariable=sb8,bd=10,insertwidth=2,justify='left')
txtsb.grid(row=3,column=1)
lblsb = Label(f1aa,font=('arial',10,'bold'),text='6 inch',bd=16,justify='left')
lblsb.grid(row=2,column=2)
txtsb=Entry(f1aa,font=('arial',8,'bold'),textvariable=sb6,bd=10,insertwidth=2,justify='left')
txtsb.grid(row=3,column=2)
lblsb = Label(f1aa,font=('arial',10,'bold'),text='4 inch',bd=16,justify='left')
lblsb.grid(row=2,column=3)
txtsb=Entry(f1aa,font=('arial',8,'bold'),textvariable=sb4,bd=10,insertwidth=2,justify='left')
txtsb.grid(row=3,column=3)
lblhb = Label(f1aa,fg='red',font=('arial',13,'bold'),text='copyrighted(c)',bd=16,justify='left')
lblhb.grid(row=3,column=4)

lblpb = Label(f1aa,font=('arial',10,'bold'),text='Paver Blocks sqft',bd=16,justify='left')
lblpb.grid(row=5,column=0)
lblpb = Label(f1aa,font=('arial',10,'bold'),text='ZigZag 80mm',bd=16,justify='left')
lblpb.grid(row=4,column=1)
txtpb=Entry(f1aa,font=('arial',8,'bold'),textvariable=pbz8,bd=10,insertwidth=2,justify='left')
txtpb.grid(row=5,column=1)
lblpb = Label(f1aa,font=('arial',10,'bold'),text='ZigZag 60mm',bd=16,justify='left')
lblpb.grid(row=4,column=2)
txtpb=Entry(f1aa,font=('arial',8,'bold'),textvariable=pbz6,bd=10,insertwidth=2,justify='left')
txtpb.grid(row=5,column=2)
lblpb = Label(f1aa,font=('arial',10,'bold'),text='I Shape 80mm',bd=16,justify='left')
lblpb.grid(row=4,column=3)
txtpb=Entry(f1aa,font=('arial',8,'bold'),textvariable=pbi8,bd=10,insertwidth=2,justify='left')
txtpb.grid(row=5,column=3)
lblpb= Label(f1aa,font=('arial',10,'bold'),text='I Shape 60mm',bd=16,justify='left')
lblpb.grid(row=4,column=4)
txtpb=Entry(f1aa,font=('arial',8,'bold'),textvariable=pbi6,bd=10,insertwidth=2,justify='left')
txtpb.grid(row=5,column=4)


# ORDER's COST


Costofhb=StringVar()
Costofsb=StringVar()
Costofpb=StringVar()


lblCostofhb = Label(f1ab,font=('arial',13,'bold'),text='Hollow Blocks Cost',bd=16,anchor='w')
lblCostofhb.grid(row=2,column=0)
txtCostofhb=Entry(f1ab,font=('arial',10,'bold'),textvariable=Costofhb,bd=10,insertwidth=2,justify='left')
txtCostofhb.grid(row=3,column=0)

lblCostofsb = Label(f1ab,font=('arial',13,'bold'),text='Solid Blocks Cost',bd=16,anchor='w')
lblCostofsb.grid(row=4,column=0)
txtCostofsb=Entry(f1ab,font=('arial',10,'bold'),textvariable=Costofsb,bd=10,insertwidth=2,justify='left')
txtCostofsb.grid(row=5,column=0)

lblCostofpb= Label(f1ab,font=('arial',13,'bold'),text='Paver Blocks Cost ',bd=16,anchor='w')
lblCostofpb.grid(row=6,column=0)
txtCostofpb=Entry(f1ab,font=('arial',10,'bold'),textvariable=Costofpb,bd=10,insertwidth=2,justify='left')
txtCostofpb.grid(row=7,column=0)


# ORDER's SUMMARY

PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

lblPaidTax = Label(f2aa,font=('arial',13,'bold'),text='GGST+SGST Tax',bd=8,anchor='w')
lblPaidTax.grid(row=2,column=0)
txtPaidTax = Entry(f2aa,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,insertwidth=2,justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal = Label(f2aa,font=('arial',16,'bold'),text='Sub Total',bd=8,anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal = Entry(f2aa,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost = Label(f2aa,font=('arial',16,'bold'),text='Total Cost',bd=8,anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost = Entry(f2aa,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)





# ORDER's INFO BUTTONS

from tkinter import messagebox

def iExit():
        qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
        if qExit > 0:
                root.destroy()
                return

def Reset():
        PaymentRef.set("")
        hb8.set(0)
        hb6.set(0)
        sb8.set(0)
        sb6.set(0)
        sb4.set(0)
        pbz8.set(0)
        pbz6.set(0)
        pbi8.set(0)
        pbi6.set(0)

        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        Costofhb.set("")
        Costofsb.set("")
        Costofpb.set("")
        na.set("")
        

def PayReference():
        x = random.randint(10034,699812)
        randomRef = str(x)
        PaymentRef.set("BILL no"+randomRef)

def CostOfOrder():
        hb8Price = float(hb8.get())
        hb6Price = float(hb6.get())
        sb8Price = float(sb8.get())
        sb6Price = float(sb6.get())
        sb4Price = float(sb4.get())     
        pbz8Price = float(pbz8.get())
        pbz6Price = float(pbz6.get())
        pbi8Price = float(pbi8.get())
        pbi6Price = float(pbi6.get())


        #value(in case of value updates do it here)
        h8=43
        h6=34
        s8=52
        s6=42
        s4=33
        pz8=65
        pz6=55
        pi8=65
        pi6=55


        
        hbb=((hb8Price*h8)+(hb6Price*h6))
        hbCost = u"\u20B9" + str("%.2f"%((hbb)))
        Costofhb.set(hbCost)

        sbb=((sb8Price*s8)+(sb6Price*s6)+(sb4Price*s4))
        sbCost = u"\u20B9" + str("%.2f"%((sbb)))
        Costofsb.set(sbCost)
        

        pbb=((pbz8Price*pz8)+(pbz6Price*pz6)+(pbi8Price*pi8)+(pbi6Price*pi6))
        pbCost = u"\u20B9" + str("%.2f"%((pbb)))
        Costofpb.set(pbCost)
        

        ToC = u"\u20B9" + str("%.2f"%((hb8Price*h8)+(hb6Price*h6)+(sb8Price*s8)+(sb6Price*s6)+(sb4Price*s4)+(pbz8Price*pz8)+(pbz6Price*pz6)+(pbi8Price*pi8)+(pbi6Price*pi6)))
        SubTotal.set(ToC)

        tp1=(((hb8Price*h8)+(hb6Price*h6)+(sb8Price*s8)+(sb6Price*s6)+(sb4Price*s4))*0.28)
        tp2=(((pbz8Price*pz8)+(pbz6Price*pz6)+(pbi8Price*pi8)+(pbi6Price*pi6))*0.18)
        tp12=(tp1+tp2)
        Tax = u"\u20B9" + str("%.2f"%((tp12)))
        gst=("%.2f"%(tp12))

        PaidTax.set(Tax)
        
        TaxPay = ((tp12))
        Cost = (((hb8Price*h8)+(hb6Price*h6)+(sb8Price*s8)+(sb6Price*s6)+(sb4Price*s4)+(pbz8Price*pz8)+(pbz6Price*pz6)+(pbi8Price*pi8)+(pbi6Price*pi6)))
        CostofItems = u"\u20B9" + str("%.2f"%(TaxPay+Cost))
        TotalCost.set(CostofItems)
        tt=("%.2f"%(TaxPay+Cost))
        
        x=random.randint(10034,699812)
        randomRef=str(x)
        PaymentRef.set("BILL no"+randomRef)

        #bill saving
        sf.write("\n\n\n\nOder id :"+ od +"\t\t\t\t Date:"+ da +"\nCustomer Name :"+inp+"\n---------------------------------------------------------------\n S.No \t Particulars\t\t \tQty \tRate \tAmount \n---------------------------------------------------------------")
        n=1

        if(0!=hb8Price):
                sf.write("\n "+ str(n)+" \t Hellow Blocks 8mm \t\t"+  str(int(hb8Price))+"\t"+str(h8)+"\t"+str(hb8Price*h8))
                n=n+1
        if(0!=hb6Price):
                sf.write("\n "+ str(n)+" \t Hellow Blocks 6mm \t\t"+  str(int(hb6Price))+"\t"+str(h6)+"\t"+str(hb6Price*h6))
                n=n+1
        if(0!=sb8Price):
                sf.write("\n "+ str(n)+" \t Solid Blocks 8mm \t\t"+  str(int(sb8Price))+"\t"+str(s8)+"\t"+str(sb8Price*s8))
                n=n+1
        if(0!=sb6Price):
                sf.write("\n "+ str(n)+" \t Solid Blocks 6mm \t\t"+  str(int(sb6Price))+"\t"+str(s6)+"\t"+str(sb6Price*s6))
                n=n+1
        if(0!=sb4Price):
                sf.write("\n "+ str(n)+" \t Solid Blocks 4mm \t\t"+  str(int(sb4Price))+"\t"+str(s4)+"\t"+str(sb4Price*s4))
                n=n+1
        if(0!=pbz8Price):
                sf.write("\n "+ str(n)+" \t Paver Blocks zigzag 8mm \t"+  str(int(pbz8Price))+"\t"+str(pz8)+"\t"+str(pbz8Price*pz8))
                n=n+1
        if(0!=pbz6Price):
                sf.write("\n "+ str(n)+" \t Paver Blocks zigzag 6mm \t"+  str(int(pbz6Price))+"\t"+str(pz6)+"\t"+str(pbz6Price*pz6))
                n=n+1
        if(0!=pbi8Price):
                sf.write("\n "+ str(n)+" \t Paver Blocks I shape 8mm \t"+  str(int(pbi8Price))+"\t"+str(pi8)+"\t"+str(pbi8Price*pi8))
                n=n+1
        if(0!=pbi6Price):
                sf.write("\n "+ str(n)+" \t Paver Blocks I shape 8mm \t"+  str(int(pbi6Price))+"\t"+str(pi6)+"\t"+str(pbi6Price*pi6))
        sf.write("\n\n\n\n\t\t\t\tSUB TOTAL\t\t"+str(Cost))
        sf.write("\n\t\t\t\tGST tax\t\t\t"+str(gst))
        sf.write("\n\n\n\n\t\t\t\t-------------------------------")
        sf.write("\n\t\t\t\tGRAND TOTAL\t\t"+str(tt))
        sf.write("\n\t\t\t\t-------------------------------")
        

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg='blue',font=('arial',16,'bold'),width=15,text='Total Cost', command =CostOfOrder).grid(row=0,column=0)

btnRefer=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Sales Reference', command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Reset',command=Reset).grid(row=1,column=0)

btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='red',font=('arial',16,'bold'),width=15,text='Exit',command=iExit).grid(row=1,column=1)





root.mainloop()
sf.close()
