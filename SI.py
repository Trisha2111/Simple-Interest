from tkinter import *

window=Tk()
window.title("Simple Interest Calculator")
window.geometry("500x400")
window.configure(bg="grey")

def calculateInterest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)

    result.destroy()
    message=Label(resultframe,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest),bg="grey",font=("Calibri",12),width=55)
    message.place(x=20,y=40)
    message.pack()


applabel=Label(window,text="SIMPLE INTEREST CALCULATOR",fg="black",bg="grey",font=("Calibri",20))
applabel.place(x=20,y=20)

principlelabel=Label(window,text="Principle in Rs",fg="black",bg="grey",font=("Calibri",12))
principlelabel.place(x=20,y=90)

principle=Entry(window,text="",width=22)
principle.place(x=200,y=92)

ratelabel=Label(window,text="Rate of interest in %",fg="black",bg="grey",font=("Calibri",12))
ratelabel.place(x=20,y=140)

rate=Entry(window,text="",width=15)
rate.place(x=200,y=142)

timelabel=Label(window,text="Time in years",fg="black",bg="grey",font=("Calibri",12))
timelabel.place(x=20,y=185)

time=Entry(window,text="",width=15)
time.place(x=200,y=187)

calculatebutton=Button(window,text="CALCULATE",fg="black",bg="grey",command=calculateInterest)
calculatebutton.place(x=20,y=250)

resultframe=LabelFrame(window,text="Result",bg="grey",font=("Calibri",12))
resultframe.pack(padx=20,pady=20)
resultframe.place(x=20,y=300)

result=Label(resultframe,text="Your Result will be displayed here",bg="grey",font=("Calibri",12),width=55)
result.place(x=20,y=20)
result.pack()

window.mainloop()

