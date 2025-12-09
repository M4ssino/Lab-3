from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from string import ascii_uppercase
from random import *
import pygame

root = Tk()

def generate(len_key):
    alpha = f'{ascii_uppercase}012345679'
    st = ''
    for i in range(len_key):
        st += choice(alpha)
    return st

def schet(key_element):
    alpha = f'{ascii_uppercase}0123456789'
    k = 0
    for character_position, current_character in enumerate(alpha, 1):
        for i in key_element.replace('-', ''):
            if i.isdigit():
                character_position += int(i)
            elif current_character == i:
                k += character_position
    return k

def generate_key():
    key = ''
    for i in [5, 4, 4]:
        key_element = generate(i)
        while not (10 <= (schet(key_element) // i) <= 15):
            print(schet(key_element) // i)
            key_element = generate(i)
        key += f'{key_element}-'
    clean_key = key.rstrip('-')
    output_label.config(text=clean_key)


root['bg'] = '#000000'
root.title('Key Generator for Hollow Knight')
root.wm_attributes('-alpha', 0.8)
root.geometry('900x600')
root.resizable(width=False, height=False)

pygame.mixer.init()
pygame.mixer.music.load("Resting Grounds.mp3")
pygame.mixer.music.play(-1)

bg_image = Image.open("HollowKnight.png")
bg_image_resized = bg_image.resize((900, 600))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo


title = Label(root,
              text='KEY GENERATOR',
              bg='black',
              fg='white',
              font=('SF Pro', 42)
              )
title.pack(pady=20)

btn = Button(
    root,
    text="Generate",
    bg="white",
    fg="black",
    font=("SF Pro", 14),
    relief="flat",
    activebackground="#f0f0f0",
    activeforeground="black",
    bd=0,
    command=generate_key
)
btn.configure(height=2, width=20)
btn.pack(pady=100)

output_label = Label(root,
                     text='',
                     bg='black',
                     fg='white',
                     font=('SF Pro', 26),
                     )
output_label.configure(height=2, width=40)
output_label.pack(pady=60)

root.eval('tk::PlaceWindow . center')
root.mainloop()