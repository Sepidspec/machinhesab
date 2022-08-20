from tkinter import *
root=Tk()
equation=StringVar()


h=Label(root,textvariable=equation,font=('Tohoma',20),pady=10)
h.grid(columnspan=4)

def set_number(num):
    equation.set(equation.get()+num)
def calculate_equation():
    eq=equation.get()
    result=eval(eq)
    equation.set(result)

   
def clear_all():
    equation.clear(0,End)         
    
btn1=Button(root,text='1',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('1'))
btn1.grid(row=1,column=0)
btn2=Button(root,text='2',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('2'))
btn2.grid(row=1,column=1)
btn3=Button(root,text='3',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('3'))
btn3.grid(row=1,column=2)
btn4=Button(root,text='4',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('4'))
btn4.grid(row=2,column=0)
btn5=Button(root,text='5',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('5'))
btn5.grid(row=2,column=1)
btn6=Button(root,text='6',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('6'))
btn6.grid(row=2,column=2)
btn7=Button(root,text='7',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('7'))
btn7.grid(row=3,column=0)
btn8=Button(root,text='8',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('8'))
btn8.grid(row=3,column=1)
btn9=Button(root,text='9',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('9'))
btn9.grid(row=3,column=2)
btn0=Button(root,text='0',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('0'))
btn0.grid(row=4,column=1)
btnclear=Button(root,text='c',width=5,height=2,font=('Tohoma',20),command=lambda:equation.set(''))
btnclear.grid(row=4,column=0)
btnequal=Button(root,text='=',width=5,height=2,font=('Tohoma',20),command=calculate_equation)
btnequal.grid(row=4,column=2)
btnplus=Button(root,text='+',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('+'))
btnplus.grid(row=1,column=3)
btnsub=Button(root,text='*',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('*'))
btnsub.grid(row=2,column=3)
btnmul=Button(root,text='-',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('-'))
btnmul.grid(row=3,column=3)
btndivid=Button(root,text='/',width=5,height=2,font=('Tohoma',20),command=lambda:set_number('/'))

btndivid.grid(row=4,column=3)



