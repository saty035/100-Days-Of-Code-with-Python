#Simple Calculator using tkinter
#by saty035

from tkinter import*    #GUI toolkit

#entering numbers
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

#Clearing the screen
def btnClearDisplay():   
    global operator
    operator=''
    text_input.set("")

#resulting output
def btnEql():    
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''


cal=Tk()
cal.title("Calculator by saty035")    #title
operator=""
text_input=StringVar()

#screen
txtDisplay=Entry(cal,font=('ariel',20,'bold'), textvariable=text_input,bd=30,insertwidth=4,bg='pink',justify='right').grid(columnspan=4)   

#buttons and operators
btn7=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='7',command=lambda:btnClick(7),bg='powder blue').grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='8',command=lambda:btnClick(8),bg='powder blue').grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='9',command=lambda:btnClick(9),bg='powder blue').grid(row=1,column=2)

addition=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='+',command=lambda:btnClick('+'),bg='powder blue').grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='4',command=lambda:btnClick(4),bg='powder blue').grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='5',command=lambda:btnClick(5),bg='powder blue').grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='6',command=lambda:btnClick(6),bg='powder blue').grid(row=2,column=2)

subtraction=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='-',command=lambda:btnClick('-'),bg='powder blue').grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='1',command=lambda:btnClick(1),bg='powder blue').grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='2',command=lambda:btnClick(2),bg='powder blue').grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='3',command=lambda:btnClick(3),bg='powder blue').grid(row=3,column=2)

multiplication=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='*',command=lambda:btnClick('*'),bg='powder blue').grid(row=3,column=3)

btn0=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('ariel',20,'bold'),text='0',command=lambda:btnClick(0),bg='powder blue').grid(row=4,column=0)
clr=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('ariel',20,'bold'),text='C',bg='powder blue',command=btnClearDisplay).grid(row=4,column=1)
eql=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('ariel',20,'bold'),text='=',bg='powder blue',command=btnEql).grid(row=4,column=2)

division=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('ariel',20,'bold'),text='/',command=lambda:btnClick('/'),bg='powder blue').grid(row=4,column=3)




#mainloop
cal.mainloop()   