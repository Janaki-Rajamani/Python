from tkinter import *
import tkinter as tk
equation=""
memory=""

class Error(Exception):
        pass

        
class ValueNotFound(Error):
        pass

def show(value):
	global equation
	equation=cal_var.get()
	equation+=value
	cal_var.set(equation)
	display.icursor(len(equation))
	print(equation)

def calc():
  global equation
  
  equation=cal_var.get()
  try:
      equation=str(eval(equation))
      cal_var.set(equation)
  except:
      equation=""
      cal_var.set(equation)
                

def clear():
	global equation
	memory=equation
	equation=""
	cal_var.set(equation)

def back():
    global equation
    equation=equation[:len(equation)-1]
    cal_var.set(equation)
    print(equation)

def valround():
        global equation
        equation=str(round(eval(equation)))
        cal_var.set(equation)

def memclr():
        global memory
        memory=""
def memread():
        global memory
        cal_var.set("")
        cal_var.set(memory)
def memstore():
        global memory
        global equation
        memory=equation
        print(memory)
def memadd():
        global memory
        global equation
       
        if (memory!=""):
                equation=str(eval(memory)+eval(equation))
                cal_var.set(equation)
               
        
        

def memsub():
        global memory
        global equation
       
        if (memory!=""):
                equation=str(eval(memory)-eval(equation))
                cal_var.set(equation)
               
      
       
         

        
        

window=Tk()
window.geometry("340x350")
window.resizable(0,0)
window.title("CALCULATOR")
window.configure(bg="grey")

cal_var=tk.StringVar()
display=Entry(window,width=30,font=(40),textvariable = cal_var)
display.place(x=2,y=8)



Button(window,text="MC",height=2, width=5,bg="yellow",command=lambda:memclr()).place(x=20,y=50)
Button(window,text="MR",height=2, width=5,bg="yellow",command=lambda:memread()).place(x=70,y=50)
Button(window,text="M+",height=2, width=5,bg="yellow",command=lambda:memadd()).place(x=120,y=50)
Button(window,text="M-",height=2, width=5,bg="yellow",command=lambda:memsub()).place(x=170,y=50)
Button(window,text="MS",height=2, width=5,bg="yellow",command=lambda:memstore()).place(x=220,y=50)
Button(window,text="Round",height=2, width=6,bg="yellow",command=lambda:valround()).place(x=270,y=50)


Button(window,text="%",height=2, width=8,bg="powder blue",command=lambda:show("%")).place(x=20,y=100)
Button(window,text="C",height=2, width=8,bg="powder blue",command=lambda:clear()).place(x=100,y=100)
Button(window,text="BACK",height=2, width=8,bg="powder blue",command=lambda:back()).place(x=180,y=100)
Button(window,text="=",height=2, width=8,bg="powder blue",command=lambda:calc()).place(x=260,y=100)

Button(window,text="+",height=2, width=8,bg="pink",command=lambda:show("+")).place(x=20,y=150)
Button(window,text="-",height=2, width=8,bg="pink",command=lambda:show("-")).place(x=100,y=150)
Button(window,text="*",height=2, width=8,bg="pink",command=lambda:show("*")).place(x=180,y=150)
Button(window,text="/",height=2, width=8,bg="pink",command=lambda:show("/")).place(x=260,y=150)

Button(window,text="7",height=2, width=8,bg="#90EE90",command=lambda:show("7")).place(x=20,y=200)
Button(window,text="8",height=2, width=8,bg="#90EE90",command=lambda:show("8")).place(x=100,y=200)
Button(window,text="9",height=2, width=8,bg="#90EE90",command=lambda:show("9")).place(x=180,y=200)
Button(window,text="%",height=2, width=8,bg="pink",command=lambda:show("%")).place(x=260,y=200)

Button(window,text="4",height=2, width=8,bg="#90EE90",command=lambda:show("4")).place(x=20,y=250)
Button(window,text="5",height=2, width=8,bg="#90EE90",command=lambda:show("5")).place(x=100,y=250)
Button(window,text="6",height=2, width=8,bg="#90EE90",command=lambda:show("6")).place(x=180,y=250)
Button(window,text=".",height=2, width=8,bg="pink",command=lambda:show(".")).place(x=260,y=250)

Button(window,text="1",height=2, width=8,bg="#90EE90",command=lambda:show("1")).place(x=20,y=300)
Button(window,text="2",height=2, width=8,bg="#90EE90",command=lambda:show("2")).place(x=100,y=300)
Button(window,text="3",height=2, width=8,bg="#90EE90",command=lambda:show("3")).place(x=180,y=300)
Button(window,text="0",height=2, width=8,bg="#90EE90",command=lambda:show("0")).place(x=260,y=300)


