from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

#boolean
click = False

#fungsi
def checker(buttons):
    global click

    #menukar huruf dari kosong ke X
    if buttons['text'] == " " and click == False:
        buttons['text'] = "X"
        click = True
    #menukar huruf dari kosong ke O
    elif buttons['text'] == " " and click == True:
        buttons['text'] = "O"
        click = False

    #semak syarat pemenang X
    elif ((button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X') or
        (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X') or
        (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X') or
        (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X') or
        (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X') or
        (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X') or
        (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X') or
        (button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X') ):
            tkinter.messagebox.showinfo("Pemenang X","Tahniah! Anda sudah menang")
            
    #semak syarat pemenang O
    elif ((button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O') or
        (button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O') or
        (button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O') or
        (button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O') or
        (button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O') or
        (button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O') or
        (button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O') or
        (button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O') ):
            tkinter.messagebox.showinfo("Pemenang O","Tahniah! Anda sudah menang")
    

#grid permainan
button1 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button1))
button1.grid(row = 0, column = 0)

button2 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button2))
button2.grid(row = 0, column = 1)

button3 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button3))
button3.grid(row = 0, column = 2)

button4 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button4))
button4.grid(row = 1, column = 0)

button5 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button5))
button5.grid(row = 1, column = 1)

button6 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button6))
button6.grid(row = 1, column = 2)

button7 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button7))
button7.grid(row = 2, column = 0)

button8 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button8))
button8.grid(row = 2, column = 1)

button9 = Button (text=" ",font = "Times 16 bold", width = 8, height = 4, command=lambda:checker(button9))
button9.grid(row = 2, column = 2)

tk.mainloop()
