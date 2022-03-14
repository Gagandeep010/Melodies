import random
from tkinter import *

from music21 import *

dir(note)

n01 = note.Note('c1')
n02 = note.Note('c#1')
n03 = note.Note('d1')
n04 = note.Note('d#1')
n05 = note.Note('e1')
n06 = note.Note('f1')
n07 = note.Note('f#1')
n08 = note.Note('g1')
n09 = note.Note('g#1')
n10 = note.Note('a1')
n11 = note.Note('a#1')
n12 = note.Note('b1')
n13 = note.Note('c2')
n14 = note.Note('c#2')
n15 = note.Note('d2')
n16 = note.Note('d#2')
n17 = note.Note('e2')
n18 = note.Note('f2')
n19 = note.Note('f#2')
n20 = note.Note('g2')
n21 = note.Note('g#2')
n22 = note.Note('a2')
n23 = note.Note('a#2')
n24 = note.Note('b2')
n25 = note.Note('c3')
n26 = note.Note('c#3')
n27 = note.Note('d3')
n28 = note.Note('d#3')
n29 = note.Note('e3')
n30 = note.Note('f3')
n31 = note.Note('f#3')
n32 = note.Note('g3')
n33 = note.Note('g#3')
n34 = note.Note('a3')
n35 = note.Note('a#3')
n36 = note.Note('b3')
n37 = note.Note('c4')
n38 = note.Note('c#4')
n39 = note.Note('d4')
n40 = note.Note('d#4')
n41 = note.Note('e4')
n42 = note.Note('f4')
n43 = note.Note('f#4')
n44 = note.Note('g4')
n45 = note.Note('g#4')
n46 = note.Note('a4')
n47 = note.Note('a#4')
n48 = note.Note('b4')
n49 = note.Note('c5')
n50 = note.Note('c#5')
n51 = note.Note('d5')
n52 = note.Note('d#5')
n53 = note.Note('e5')
n54 = note.Note('f5')
n55 = note.Note('f#5')
n56 = note.Note('g5')
n57 = note.Note('g#5')
n58 = note.Note('a5')
n59 = note.Note('a#5')
n60 = note.Note('b5')
n61 = note.Note('c5')

c_Mc = chord.Chord([n01, n05, n08])
d_Mc = chord.Chord([n03, n07, n10])
e_Mc = chord.Chord([n05, n09, n11]) 
f_Mc = chord.Chord([n06, n10, n13])
g_Mc = chord.Chord([n08, n12, n15])
a_Mc = chord.Chord([n10, n14, n17])
b_Mc = chord.Chord([n12, n16, n19])

cM_s = [n25, n27, n29, n30, n32, n34, n36, n37]
dM_s = [n27, n29, n31, n32, n34, n36, n38, n39]
eM_s = [n29, n31, n33, n34, n36, n38, n40, n41]
fM_s = [n30, n32, n34, n35, n37, n39, n41, n42]
gM_s = [n32, n34, n36, n37, n39, n41, n43, n44]
aM_s = [n34, n36, n38, n39, n41, n43, n45, n46]
bM_s = [n36, n38, n40, n41, n43, n45, n47, n48]

built_song = []
i = 1

print('Welcome To Melodies With Python')
ref = input('Enter The Scale In Which You Want The New Melody:')
if ref in 'Cc':
    while i:
        a = random.choice(cM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

if ref in 'dD':
    while i:
        a = random.choice(dM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

if ref in 'eE':
    while i:
        a = random.choice(eM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

if ref in 'fF':
    while i:
        a = random.choice(fM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

if ref in 'gG':
    while i:
        a = random.choice(gM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break
        
if ref in 'aA':
    while i:
        a = random.choice(aM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

if ref in 'bB':
    while i:
        a = random.choice(bM_s)
        if a in built_song:
            continue
        built_song.append(a)
        if len(built_song) != 5:
            i = i + 1
        else:
            break

song = stream.Stream()
song.append(built_song)

song.show('midi')

b = input('enter y if you like the music and want to see the notes:')
if b in 'Yy':
    print(built_song)
else:
    pass
