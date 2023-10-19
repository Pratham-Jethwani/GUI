from tkinter import*
import math
a=Tk()
a.title("MY CALCULATOR")
e=Entry(a,width=40,borderwidth=5,bg="peachpuff",fg="black",border=5)
e.grid(row=0,column=0,columnspan=4,padx=30,pady=15)

def click(i):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(i))

def clr():
    e.delete(0,END)

def back():
    a=str(e.get())
    l=len(a)-1
    e.delete(l)
    

def equal():
    b=e.get()
    e.delete(0,END)
    if operation=="addition":
        e.insert(0,float(a)+float(b))
    if operation=="substraction":
        e.insert(0,float(a)-float(b))
    if operation=="multiplication":
        e.insert(0,float(a)*float(b))
    if operation=="division":
        e.insert(0,float(a)/float(b))
    if operation=="power":
        e.insert(0,float(a)**float(b))
    if operation=="root":
        e.insert(0,math.sqrt(float(a)))
def add():
    one=e.get()
    global a
    global operation
    operation="addition"
    a=float(one)
    e.delete(0,END)
def subs():
    one=e.get()
    global a
    global operation
    operation="substraction"
    a=float(one)
    e.delete(0,END)
def mul():
    one=e.get()
    global a
    global operation
    operation="multiplication"
    a=float(one)
    e.delete(0,END)
def div():
    one=e.get()
    global a
    global operation
    operation="division"
    a=float(one)
    e.delete(0,END)
def pow():
    one=e.get()
    global a
    global operation
    operation="power"
    a=float(one)
    e.delete(0,END)
    
def sqrt():
    one=e.get()
    global a
    global operation
    operation="root"
    a=float(one)
    e.delete(0,END)
b0=Button(a,text="0",padx=44,pady=30,command=lambda:click(0),bg="dark gray",fg="black")
b1=Button(a,text="1",padx=44,pady=30,command=lambda:click(1),bg="dark gray",fg="black")
b2=Button(a,text="2",padx=48,pady=30,command=lambda:click(2),bg="dark gray",fg="black")
b3=Button(a,text="3",padx=50,pady=30,command=lambda:click(3),bg="dark gray",fg="black")
b4=Button(a,text="4",padx=44,pady=30,command=lambda:click(4),bg="dark gray",fg="black")
b5=Button(a,text="5",padx=48,pady=30,command=lambda:click(5),bg="dark gray",fg="black")
b6=Button(a,text="6",padx=50,pady=30,command=lambda:click(6),bg="dark gray",fg="black")
b7=Button(a,text="7",padx=44,pady=30,command=lambda:click(7),bg="dark gray",fg="black")
b8=Button(a,text="8",padx=48,pady=30,command=lambda:click(8),bg="dark gray",fg="black")
b9=Button(a,text="9",padx=50,pady=30,command=lambda:click(9),bg="dark gray",fg="black")
b_po=Button(a,text=".",padx=50,pady=30,command=lambda:click("."),bg="dim gray",fg="black")
b_add=Button(a,text="+",padx=48,pady=30,command=add,bg="dim gray",fg="white")
b_equal=Button(a,text="=",padx=54,pady=30,command=equal,bg="dim gray",fg="white")
b_clc=Button(a,text="clr",padx=42,pady=30,command=clr,bg="dim gray",fg="white")
b_subs=Button(a,text="-",padx=50,pady=30,command=subs,bg="dim gray",fg="white")
b_div=Button(a,text="%",padx=52,pady=30,command=div,bg="dim gray",fg="white")
b_mul=Button(a,text="*",padx=54,pady=30,command=mul,bg="dim gray",fg="white")
b_power=Button(a,text='^',padx=54,pady=30,command=pow,bg="dim gray",fg="white")
b_root=Button(a,text="sq.rt",padx=46,pady=30,command=sqrt,bg="dim gray",fg="white")
b_ba=Button(a,text="back",padx=42,pady=30,command=back,bg="dim gray",fg="white")
b1.grid(row=2,column=0,columnspan=1)
b2.grid(row=2,column=1,columnspan=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
b0.grid(row=5,column=0)
b_add.grid(row=1,column=1)
b_equal.grid(row=5,column=3)
b_clc.grid(row=1,column=0,columnspan=1)
b_subs.grid(row=1,column=2)
b_div.grid(row=1,column=3)
b_mul.grid(row=2,column=3,columnspan=1)
b_power.grid(row=3,column=3,columnspan=1)
b_root.grid(row=4,column=3)
b_po.grid(row=5,column=1,columnspan=1)
b_ba.grid(row=5,column=2)
a.mainloop()