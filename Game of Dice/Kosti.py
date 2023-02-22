from tkinter import*
import random, time

def bros():
    x = random.choice(['Files\\b.png', 'Files\\b2.png', 'Files\\b3.png', 'Files\\b4.png', 'Files\\b5.png', 'Files\\b6.png'])
    return x

def img(event):
    global b1, b2
    for i in range(15):
        b1 = PhotoImage(file=bros())
        b2 = PhotoImage(file=bros())
        lab1 ['image'] = b1
        lab2 ['image'] = b2
        root.update()
        time.sleep(0.13)




root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Нажми для броска!')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file=('Files\iconka.png')))
font = PhotoImage(file=('Files\holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor =CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor =CENTER)
root.bind('<1>', img)
img('event')

root.mainloop()
