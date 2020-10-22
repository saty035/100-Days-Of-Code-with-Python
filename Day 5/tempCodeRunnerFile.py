from tkinter import*    #GUI toolkit

cal=Tk()
cal.title("Calculator by saty035")
operator=""
text_input=StringVar()

txtDisplay=Entry(cal,font=('ariel',20,'bold'), textvariable=text_input,bd=30,insertwidth=4,bg='pink',justify='right').grid(columnspan=4)


btn7=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='7').grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='8').grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='9').grid(row=1,column=2)

addition=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='+').grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='4').grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='5').grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='6').grid(row=2,column=2)

subtraction=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='-').grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='1').grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='2').grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='3').grid(row=3,column=2)

multiplication=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='*').grid(row=3,column=3)

btn0=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='0').grid(row=4,column=0)
clr=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='C').grid(row=4,column=1)
eql=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='=').grid(row=4,column=2)
division=Button(cal,padx=16,bd=8,fg='black',font=('ariel',20,'bold'),text='/').grid(row=4,column=3)





cal.mainloop()