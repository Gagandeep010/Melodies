import pygame
import time
from tkinter import *
from datetime import datetime

import pygame

pygame.init()
root = Tk()
root.title("Music Box")
root.geometry("1235x700")
root.configure(background="white")

ABC = Frame(
	root,
	bg="powder blue",
	bd=20,
	relief=RIDGE
)
ABC.grid()

ABC1 = Frame(ABC, bg="powder blue", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 = Frame(
	ABC,
	bg="powder blue",
	relief=RIDGE
)
ABC2.grid()
ABC3 = Frame(ABC, bg="powder blue", relief=RIDGE)
ABC3.grid()

strl = StringVar()
strl.set("Just Like Music")
date1 = StringVar()
time1 = StringVar()
date1.set(time.strftime("%d/%m/%Y"))
time1.set(time.strftime("%H:%M:%S"))
#===================================================================================================================================================================================

def value_cs():
	strl.set("C#")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\C#.wav")
	song.play()


def value_ds():
	strl.set("D#")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\D#.wav")
	song.play()


def value_fs():
	strl.set("F#")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\F#.wav")
	song.play()


def value_gs():
	strl.set("G#")
	song= pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\G#.wav")
	song.play()
	return


def value_bb():
	strl.set("Bb")
	song= pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\Bb.wav")
	song.play()
	return


def value_cs1():
	strl.set("C#1")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\C#1.wav")
	song.play()
	return


def value_ds1():
	strl.set("D#1")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\D#1.wav")
	song.play()
	return


def value_c():
	strl.set("C")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\C.wav")
	song.play()
	return


def value_d():
	strl.set("D")
	song = pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\D.wav")
	song.play()
	return


def value_e():
	strl.set("E")
	song= pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\E.wav")
	song.play()
	return


def value_f():
	strl.set("F")
	song= pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\F.wav")
	song.play()
	return


def value_g():
	strl.set("G")
	song= pygame.mixer.Sound(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\G.wav")
	song.play()
	return


def value_a():
	strl.set("A")
	song=pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\A.wav")
	song.play()
	return


def value_b():
	strl.set("B")
	song = pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\B.wav")
	song.play()
	return


def value_c1():
	strl.set("C1")
	song= pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\C1.wav")
	song.play()
	return


def value_d1():
	strl.set("D1")
	song= pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\D1.wav")
	song.play()
	return


def value_e1():
	strl.set("E1")
	song = pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\E1.wav")
	song.play()
	return


def value_f1():
	strl.set("F1")
	song = pygame.mixer(r"C:\Users\ADMIN\Downloads\Melody\melodies\Music\F1.wav")
	song.play()
	return

#===================================================================================================================================================================================




Label(ABC1, text = "Piano Musical Keys", font = ('arial', 25 , 'bold'), padx = 8, pady = 8, bd = 4, bg = "powder blue",
      fg = "white", justify = CENTER).grid(row = 0, column = 0, columnspan = 11)

#===================================================================================================================================================================================


txtDate = Entry(ABC1, textvariable = date1, font = ('arial', 18, 'bold'), bd = 34, bg = "powder blue",
      fg = "black", width = 28, justify = CENTER).grid(row = 1, column = 0, pady = 1)
txtDisplay = Entry(ABC1, textvariable = strl, font = ('arial', 18, 'bold'), bd = 34, bg = "powder blue",
      fg = "black", width = 28, justify = CENTER).grid(row = 1, column = 1, pady = 1)
txtTime = Entry(ABC1, textvariable = time1, font = ('arial', 18, 'bold'), bd = 34, bg = "powder blue",
      fg = "black", width = 28, justify = CENTER).grid(row = 1, column = 2, pady = 1)
#===================================================================================================================================================================================
btnCs = Button(ABC2,  height = 6, width = 6, bd = 4, text = "C#", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white",command=value_cs)
btnCs.grid(row = 0, column = 0, padx = 5, pady = 5)

btnDs = Button(ABC2,  height = 6, width = 6, bd = 4, text = "D#", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white", command= value_ds)
btnDs.grid(row = 0, column = 2, padx = 5, pady = 5)

btnSpace2 = Button(ABC2, state = DISABLED,  height = 6, width = 2, bg = "powder blue", relief = FLAT)
btnSpace2.grid(row = 0, column = 3, padx = 0, pady = 0)

btnFs = Button(ABC2,  height = 6, width = 6, bd = 4, text = "F#", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white", command= value_fs)
btnFs.grid(row = 0, column = 4, padx = 5, pady = 5)

btnGs = Button(ABC2,  height = 6, width = 6, bd = 4, text = "G#", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white", command= value_gs)
btnGs.grid(row = 0, column = 6, padx = 5, pady = 5)

#===================================================================================================================================================================================

btnBb = Button(ABC2,  height = 6, width = 6, bd = 4, text = "Bb", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white",command= value_bb)
btnBb.grid(row = 0, column = 8, padx = 5, pady = 5)

btnSpace5 = Button(ABC2, state = DISABLED,  height = 6, width = 2, bg = "powder blue", relief = FLAT)
btnSpace5.grid(row = 0, column = 9, padx = 0, pady = 0)

btnCs1 = Button(ABC2,  height = 6, width = 6, bd = 4, text = "C#1", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white",command= value_cs1)
btnCs1.grid(row = 0, column = 10, padx = 5, pady = 5)

btnDs1 = Button(ABC2,  height = 6, width = 6, bd = 4, text = "D#1", font = ('arial', 18 , 'bold'), bg = "black",  fg = "white",command= value_ds1)
btnDs1.grid(row = 0, column = 12, padx = 5, pady = 5)

#===================================================================================================================================================================================
btnC = Button(ABC3,  height = 8, width = 6, bd = 4, text = "C", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black" ,command= value_c)
btnC.grid(row = 0, column = 0, padx = 5, pady = 5)

btnD = Button(ABC3,  height = 8, width = 6, bd = 4, text = "D", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command= value_d)
btnD.grid(row = 0, column = 1, padx = 5, pady = 5)

btnE = Button(ABC3,  height = 8, width = 6, bd = 4, text = "E", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command= value_e)
btnE.grid(row = 0, column = 2, padx = 5, pady = 5)

btnF = Button(ABC3,  height = 8, width = 6, bd = 4, text = "F", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command = value_f)
btnF.grid(row = 0, column = 3, padx = 5, pady = 5)

btnG = Button(ABC3,  height = 8, width = 6, bd = 4, text = "G", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black" ,command= value_g)
btnG.grid(row = 0, column = 4, padx = 5, pady = 5)

btnA = Button(ABC3,  height = 8, width = 6, bd = 4, text = "A", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command= value_a)
btnA.grid(row = 0, column = 5, padx = 5, pady = 5)

btnB = Button(ABC3,  height = 8, width = 6, bd = 4, text = "B", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command= value_b)
btnB.grid(row = 0, column = 6, padx = 5, pady = 5)

btnC1 = Button(ABC3,  height = 8, width = 6, bd = 4, text = "C1", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command = value_c1)
btnC1.grid(row = 0, column = 7, padx = 5, pady = 5)

btnD1 = Button(ABC3,  height = 8, width = 6, bd = 4, text = "D1", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black" ,command = value_d1)
btnD1.grid(row = 0, column = 8, padx = 5, pady = 5)

btnE1 = Button(ABC3,  height = 8, width = 6, bd = 4, text = "E1", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command = value_e1)
btnE1.grid(row = 0, column = 9, padx = 5, pady = 5)

btnF1 = Button(ABC3,  height = 8, width = 6, bd = 4, text = "F1", font = ('arial', 18 , 'bold'), bg = "white",  fg = "black",command = value_f1)
btnF1.grid(row = 0, column = 10, padx = 5, pady = 5)

root.mainloop()
