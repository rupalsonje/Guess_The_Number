from tkinter import *
from random import randint

root=Tk()
root.title('Guess The Number')
root.geometry('924x400')

x = randint(1, 100)

def delete():
    global x
    exit.destroy()
    retry.destroy()
    x = randint(1, 100)
    newgame


def newgame():
    f=[]
    guesses = [0]

    def guess():
        global exit, retry, output
        i=0
        try:
            no=int(nom.get())
            nom.delete(0,END)
            guesses.append(no)
            if no < 1 or no > 100:
                z='OUT OF BOUNDS! TRY AGAIN'
            elif no == x:
                z='CONGRATULATIONS, YOU GUESSED IT RIGHT'
                i=1
            elif guesses[-2]:
                if abs(x-no) < abs(x-guesses[-2]):
                    z="WARMER"
                else:
                    z='COLDER'
            else:
                if (x-no) <= 10:
                    z='WARM!'
                else:
                    z='COLD!'
        except ValueError:
            return
        f.append(z)
        rec=''
        for d in f:
            rec += str(d) + '\n'
        output=Label(root,text=rec,pady=5)
        output.grid(row=3, column=0,columnspan=2)
        if i==1:
            f.append('\n')
            f.append('--------NEWGAME---------')
            f.append('\n')
            exit = Button(root, text='EXIT', padx=20, pady=10, command=lambda: root.destroy(),font='Helvetica 8 bold',bg='#ff9754')
            exit.grid(row=4, column=1, padx=5, pady=10)
            retry = Button(root, text='PLAY AGAIN!', padx=20, pady=10, command=delete, font='Helvetica 8 bold',bg='#ff9754')
            retry.grid(row=4, column=0, padx=5, pady=10)

    lbl.destroy()
    newgame.destroy()
    quit.destroy()
    root.geometry('540x600')
    root.config(background="#DFFBF4")
    rule=['WELCOME TO GUESS ME!',"I'm thinking of a number between 1 and 100","If your guess is more than 10 away from my number, I'll tell you you're COLD",
          "If your guess is within 10 of my number, I'll tell you you're WARM","If your guess is farther than your most recent guess, I'll say you're getting COLDER",
          "If your guess is closer than your most recent guess, I'll say you're getting WARMER","LET'S PLAY!"]
    rl=''
    for p in rule:
        rl += p + '\n'
    rules=Label(root,text=rl,pady=5,width=70,font='Helvetica 9 bold',bg='#7ebdb4')
    rules.grid(row=0, column=0,columnspan=2, padx=(20,0),pady=(10,10))
    lbl1=Label(root,text='guess the number',pady=5,width=25,font='Helvetica 10 bold',bg='#f6d743')
    lbl1.grid(row=1, column=0, padx=20,pady=(20, 15))
    global nom
    nom=Entry(root,width=30)
    nom.grid(row=1, column=1, padx=20,pady=(15, 15))
    guess = Button(root, text='guess', padx=20, pady=10, command=guess, bg='#e4e4e4')
    guess.grid(row=2, column=0,columnspan=2, padx=5, pady=10)


lbl=Label(root,text='GUESS THE NUMBER',padx=10,pady=30,width=60,bg='#63b7af',font='Helvetica 18 bold')
lbl.grid(row=0,column=0,pady=(0,30))

newgame=Button(root,text='NEW GAME',padx=10,pady=10,command=newgame,bg='white')
newgame.grid(row=1,column=0,padx=10,pady=(10,20))

quit=Button(root,text='EXIT',padx=28,pady=10,command=root.destroy,bg='white')
quit.grid(row=2,column=0,padx=10,pady=10)

root.mainloop()