from tkinter import*
import tkinter as tk
import math
a=Tk()
a.title("Astronaut Mass Calculator")

option=["Mercury","Venus","Moon","Mars","IO","Europa","Ganymede","Callisto"]
mass_multipliers = {"Mercury": 0.378, "Venus": 0.907, "Moon": 0.166,"Mars":0.377,"IO":0.1835,"Europa":0.1335,"Ganymede":0.1448,"Callisto":0.1264}

label1=Label(a,text="Destination")
label1.grid(row=0,column=0)

clicked=tk.StringVar(value="Moon")
clicked.set("select")
drop=OptionMenu(a,clicked,*option)
drop.grid(row=1,column=0)



    
    




label3=Label(a,text="Mass allowance")
label4=Label(a,text="Crew: 100 Kg")
label5=Label(a,text="Mission Specialist: 150 Kg")
label3.grid(row=3,column=0)
label4.grid(row=4,column=0)
label5.grid(row=5,column=0)

label6=Label(a,text="Tool Weights")
label6.grid(row=0,column=1)

p1=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p1.grid(row=1,column=1)

p2=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p2.grid(row=2,column=1)

p3=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p3.grid(row=3,column=1)

p4=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p4.grid(row=4,column=1)

p5=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p5.grid(row=5,column=1)

p6=Entry(a,width=10,bg="peachpuff",fg="black",border=5)
p6.grid(row=6,column=1)




def Calculate():
    crew_max=100
    #a=p1.astype(float)
    #print(a)

#defining button to perform operation
b0=Button(a,text="Calculate",command=Calculate())
b1=Button(a,text="Exit")
b0.grid(row=7,column=0,padx=0,pady=5)
b1.grid(row=8,column=0,padx=0,pady=5)

label7=Label(a,text="Available Mass")
label7.grid(row=0,column=3)


#defining text variable to display the result
p1_available=tk.IntVar()
p2_available=tk.IntVar()
p3_available=tk.IntVar()
p4_available=tk.IntVar()
p5_available=tk.IntVar()
p6_available=tk.IntVar()

p1mass=tk.Label(a,textvariable=p1_available)
p2mass=tk.Label(a,textvariable=p2_available)
p3mass=tk.Label(a,textvariable=p3_available)
p4mass=tk.Label(a,textvariable=p4_available)
p5mass=tk.Label(a,textvariable=p5_available)
p6mass=tk.Label(a,textvariable=p6_available)



















a.mainloop()