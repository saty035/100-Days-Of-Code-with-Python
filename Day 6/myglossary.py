#My Glosary project
#by saty035

from tkinter import *

#key own functon
def click():
    entered_text=textentry.get() 
    output.delete(0.0,END)
    try:
        Definition=dic[entered_text]
    except:
        Definition='Sorry, there is no word like that'

    output.insert(END,Definition)

#exit function
def close_window():
    window.destroy()
    exit()


window=Tk()
window.title('My Programing Glossary')
window.configure(bg='silver')

#my photo
photo1=PhotoImage(file='images.gif')
Label (window,image=photo1,bg='silver').grid(row=0,column=0,sticky=N)  #sticky=north

#create label
Label(window,text='Enter the word you would like to define for :',bg='black',fg='gold',font='ariel 12 bold').grid(row=1,column=0,stick=W)

#text entry
textentry=Entry(window,width=20,bg='black',fg='white')
textentry.grid(row=2,column=0,sticky=W)

#submit button
Button(window,text='SUBMIT',width=6,command=click).grid(row=3,column=0,sticky=W)

#create another label
Label(window,text='Definition: ',bg='black',fg='gold',font='ariel 12 bold').grid(row=4,column=0,sticky=W)

#text box
output=Text(window,width=75,height=6,wrap=WORD,bg='white',fg='red')
output.grid(row=5,column=0,columnspan=2,sticky=W)

#dictionary
dic={'algorithm':'a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.','bug':'an error in a computer program or system.','debug':'identify and remove errors from (computer hardware or software).'}


#exit label
Label(window,text="Click to Exit",bg='black',fg='gold' ,font='ariel 12 bold').grid(row=6,column=0,sticky=W)

#exit button
#submit button
Button(window,text='EXIT',width=6,command=close_window).grid(row=7,column=0,sticky=W)


#mainloop
window.mainloop()