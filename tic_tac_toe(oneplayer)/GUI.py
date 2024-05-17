from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Tic Tac Toe")
window.geometry("300x300")

lbl = Label(window,text="Tic Tac Toe Game",bg='blue',font=("comicsans","10"))
lbl.grid(row = 0 , column = 0)
lbl = Label(window,text="player1: X",font=("comicsans","10"))
lbl.grid(row = 2 , column = 0)
lbl = Label(window,text="player2: O",font=("comicsans","10"))
lbl.grid(row = 3 , column = 0)

turn = 1

def click_btn1():
    global turn
    if btn1['text']==" ":
        if turn == 1:
            turn = 2
            btn1['text']='X'
        elif turn == 2:
            turn = 1
            btn1['text']='O'
        check()
def click_btn2():
    global turn
    if btn2['text']==" ":
        if turn == 1:
            turn = 2
            btn2['text']='X'
        elif turn == 2:
            turn = 1
            btn2['text']='O'
        check()

def click_btn3():
    global turn
    if btn3['text'] == " ":
        if turn == 1:
            turn = 2
            btn3['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn3['text'] = 'O'
        check()

def click_btn4():
    global turn
    if btn4['text'] == " ":
        if turn == 1:
            turn = 2
            btn4['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn4['text'] = 'O'
        check()

def click_btn5():
    global turn
    if btn5['text'] == " ":
        if turn == 1:
            turn = 2
            btn5['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn5['text'] = 'O'
        check()

def click_btn6():
    global turn
    if btn6['text'] == " ":
        if turn == 1:
            turn = 2
            btn6['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn6['text'] = 'O'
        check()

def click_btn7():
    global turn
    if btn7['text'] == " ":
        if turn == 1:
            turn = 2
            btn7['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn7['text'] = 'O'
        check()

def click_btn8():
    global turn
    if btn8['text'] == " ":
        if turn == 1:
            turn = 2
            btn8['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn8['text'] = 'O'
        check()

def click_btn9():
    global turn
    if btn9['text'] == " ":
        if turn == 1:
            turn = 2
            btn9['text'] = 'X'
        elif turn == 2:
            turn = 1
            btn9['text'] = 'O'
        check()

flag = 1
def check():
    global flag
    b1 = btn1['text']
    b2 = btn2['text']
    b3 = btn3['text']
    b4 = btn4['text']
    b5 = btn5['text']
    b6 = btn6['text']
    b7 = btn7['text']
    b8 = btn8['text']
    b9 = btn9['text']
    flag = flag +1


    #check rows
    if b1==b2 and b1==b3 and b1=='X' or b1==b2 and b1==b3 and b1=='O' :
        win(b1)
    if b4==b5 and b4==b6 and b4=='X' or b4==b5 and b4==b6 and b4=='O':
        win(b4)
    if b7==b8 and b8==b9 and b7=='X' or b7==b8 and b8==b9 and b7=='O':
        win(b7)

    #check colums
    if b1==b4 and b1==b7 and b1=='X' or b1==b4 and b1==b7 and b1=='O':
        win(b7)
    if b2==b3 and b2==b8 and b2=='X' or b2==b3 and b2==b8 and b2=='O':
        win(b2)
    if b3==b6 and b3==b9 and b3=='X' or b3==b6 and b3==b9 and b3=='O':
        win(b3)

    #check diagonals
    if b1==b5 and b1==b9 and b1=='X' or b1==b5 and b1==b9 and b1=='O' :
        win(b1)
    if b3==b5 and b3==b7 and b3=='X' or b3==b5 and b3==b7 and b3=='O' :
        win(b3)
    if flag == 10:
        messagebox.showinfo("Tie",'Game Over')
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program

def reset():
    global turn
    turn = 1
    btn1['text']=" "
    btn2['text'] = " "
    btn3['text'] = " "
    btn4['text'] = " "
    btn5['text'] = " "
    btn6['text'] = " "
    btn7['text'] = " "
    btn8['text'] = " "
    btn9['text'] = " "

btn1 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn1)
btn1.grid(row=1, column=1)
btn2 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn2)
btn2.grid(row=1, column=2)
btn3 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn3)
btn3.grid(row=1, column=3)
btn4 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn4)
btn4.grid(row=2, column=1)
btn5 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn5)
btn5.grid(row=2, column=2)
btn6 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn6)
btn6.grid(row=2, column=3)
btn7 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn7)
btn7.grid(row=3, column=1)
btn8 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn8)
btn8.grid(row=3, column=2)
btn9 = Button(window,text=" ",fg='black', bg='white', width=3, height=1, font=("comicsans","10"),command=click_btn9)
btn9.grid(row=3, column=3)
reset_btn = Button(window,text="Reset",fg='white',bg='black',width=5,height=1,font=("comicsans","10"),command=reset)
reset_btn.grid(row=16,column=16)

mainloop()

