from tkinter import *
import random
root = Tk()
root.title('X , O')
p=['X','O']
player=random.choice(p)
lbl=Label(root,text='turn ('+player+')',font='Arial 21')
lbl.pack()

def dor(row,col):
    global player
    if btn[row][col]['text']=='' and faz()==False:
        btn[row][col]['text']=player
        if player=='X':
            if faz()==False:
                player='O'
                lbl['text']='turn ('+player+')'
            elif faz()==True:
                lbl['text']='X is Winner!'
        elif player=='O':
            if faz()==False:
                player='X'
                lbl['text']='turn ('+player+')'
        if faz()==True:
            lbl['text']=player+' is Winner!'
        elif faz()=='tie':
            for row in range(3):
                for col in range(3):
                    btn[row][col]['bg']='red'
                    btn[row][col]['bg']='silver'
                    btn[row][col]['bg']='red'
            lbl['text']='No Winner'
            
            
def faz():
    for row in range(3):
        if btn[row][0]['text']==btn[row][1]['text']==btn[row][2]['text']!='':
            btn[row][0]['bg']=btn[row][1]['bg']=btn[row][2]['bg']='skyblue'
            return True
    for col in range(3):
        if btn[0][col]['text']==btn[1][col]['text']==btn[2][col]['text']!='':
            btn[0][col]['bg']=btn[1][col]['bg']=btn[2][col]['bg']='skyblue'
            return True
    if btn[0][0]['text']==btn[1][1]['text']==btn[2][2]['text']!='':
        btn[0][0]['bg']=btn[1][1]['bg']=btn[2][2]['bg']='skyblue'
        return True
    elif btn[0][2]['text']==btn[1][1]['text']==btn[2][0]['text']!='':
        btn[0][2]['bg']=btn[1][1]['bg']=btn[2][0]['bg']='skyblue'
        return True
    elif kls()==True:
        return 'tie'
    else:
        return False

def kls():
    so=9
    for row in range(3):
        for col in range(3):
            if btn[row][col]['text']!='':
                so-=1
    if so==0:
        return True
    else:
        return False
            
def eid():
    for row in range(3):
        for col in range(3):
            btn[row][col]['text']=''
            lbl['text']='turn ('+player+')'
            btn[row][col]['bg']='silver'

b=Button(root,text='restart',font='Arial 15',bg='red',width=7,command=eid)
b.pack()
btn=[[0,0,0],[0,0,0],[0,0,0]]
btnf=Frame(root)
btnf.pack()
for row in range(3):
    for col in range(3):
        btn[row][col]=Button(btnf,width=15,height=7,bg='silver',command=lambda row =row, col=col:dor(row,col))
        btn[row][col].grid(row=row,column=col)

root.mainloop()