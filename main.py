import logging
import os
import sys
import time
import tkinter as tk    
from sub import *
width,height=1366,780
events = []
a,b,m,co,pic_no= 80,80,0,0,1
global n
n = 0
lx,ly = 110,150
j =""
re = 0
guess = []
window = tk.Tk()
window.title("Hangman")
iframe = tk.Frame(master = window, width = (626/1000) * width, height = (71/100 )*height, bg = "black")
oframe = tk.Frame(master = window, width  = (366/1000)*width, height = (71/100 )*height , bg = "white")
iframe.pack(fill = tk.Y, side = tk.LEFT, expand = "True")
oframe.pack(fill = tk.Y, side =  tk.RIGHT, expand = "True")
canvas = tk.Canvas(master = oframe, bg="white", width=550, height=750)
canvas2 = tk.Canvas(master = iframe, bg="black", width=900, height=750)
def setup():
    global chosen,w,re
    if re > 0: 
        chosen.clear()
        guess.clear()
    chosen = choose_word()
    keys(65,75,80,300,50)  
    keys(75,84,80,380,100)
    keys(84,91,80,460,150)
    hangman(1)
    
    n = 0
    w = (800-lx)//(len(chosen))
    for i in range(len(chosen)):
        temp_var = canvas2.create_line(lx + (n*w),ly,lx + (n*w) +w//2,ly,fill = "white",width = 5)
        canvas2.pack()
        n+=1
    window.resizable(width = "True", height = "True")
    window.mainloop()

def onClick(i):   
    j = chr(i)
    global pic_no,var_n,background_n,co
    # Game
    k = 0
    if j in chosen and j != "!" :
        for l in range(len(chosen)):   
            if chosen[l] == str(j) and pic_no < 7 and co <len(chosen):
                k = l
                print(co)
                if guess.count(chosen[l]) < chosen.count(chosen[l]):
                    co = co +1 
                    guess.append(chosen[l])
                if co==len(chosen):
                    print("final",co)
                    c=canvas.create_text(0,0,text = "YOU WIN!",font=('Times New Roman','25','bold'), fill = "green")
                    canvas.coords(c,250 , 150)
                    canvas.pack()   
                    re_button()
                    guess.clear()
                    print("Works")
                c=canvas2.create_text(0,0,text = chosen[l],font=('Times New Roman','30'), fill = "green")
                canvas2.coords(c,lx + k*w + w//8+ 15, ly-20)
                canvas2.pack()
                if chosen.count(chosen[l]) == guess.count(chosen[l]):    
                    guess.append(chosen[l])
                
                
    if j not in chosen and j != "!" and pic_no <=7:
        pic_no = pic_no + 1
        print("Picture on display: ",pic_no)
        hangman(pic_no)
        c=canvas2.create_text(0,0,text = str(j),font=('Times New Roman','30'), fill = "red")
        canvas2.coords(c,150 + (pic_no*50), ly+400)
        canvas2.pack()
    if j == "!":
        canvas.delete('all')
        canvas2.delete('all')
        co,pic_no=0,1
        choose_word()
        setup()
        restart()

def hangman(cross):
    global pic_no,var_n,background_n,co
    if pic_no < 7 and co <len(chosen):
        fn = "Hangman" + str(cross) +".png"
        background_n = tk.PhotoImage(file=fn)
        var_n = canvas.create_image(150,400,image=background_n)
        canvas.coords(var_n,300,450)
        canvas.itemconfig(var_n, image = background_n)
        canvas.pack()
    if pic_no >= 7 and co <len(chosen):
        fn = "Hangman7.png"
        background_n = tk.PhotoImage(file=fn)
        var_n = canvas.create_image(150,400,image=background_n)
        canvas.coords(var_n,300,450)        
        c=canvas.create_text(0,0,text = "You lose, Better luck next time!",font=('Times New Roman','15','bold'), fill ="red")
        e=canvas.create_text(0,0,text = chosen,font=('Times New Roman','15','bold'), fill ="green")
        canvas.coords(c,250 , ly)
        canvas.coords(e,250,ly+300)
        canvas.pack()
        print("You lose, Better luck next time!") 
        re_button()
        guess.clear() 
        
    return
    
def keys(ini,fin,a,b,ipx):
    m =0
    global buttons 
    buttons = []
    for i in range(ini,fin):
        s = chr(i)
        button = tk.Button(
            text = s,
            width = 7,
            height = 3,
            master = iframe,
            fg = "white",
            bg = "blue",
            command = lambda i=i: onClick(i)
        )
        button.pack()
        buttons.append(button)  
        button.place(x = ipx + (a*m),y = b)
        m+=1

def restart():
    global re
    re +=1
    guess.clear()
    chosen.clear()


def re_button():
    j = "!"
    i = ord(j)
    button = tk.Button(
            text = "Restart",
            name = "!",
            width = 10,
            height = 3,
            master = oframe,
            fg = "white",
            bg = "blue",
            command = lambda i=i: onClick(i)
            )
    button.pack()
        
    buttons.append(button)  
    button.place(x=215,y=ly + 400)

if __name__ == "__main__":
    setup()


