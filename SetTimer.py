import time
import tkinter as tk
import playsound
import pygame
from tkinter import *
from tkinter.messagebox import _show
from tkinter import ttk
from tkinter import *
from pygame.locals import *
from tkinter import *
from os import startfile

window = tk.Tk()
window.title("SetTimer")
window.geometry('480x320')
window.iconbitmap('icon (1).ico')

_show("SetTimer", "Limits:\n\nhour = 24\n\nminute = 60\n\nsecond = 60")


def timer():
      current_time = ttk.Label(window, text=time.strftime('%I:%M:%S'))
      current_time.pack()
      current_time.place(x=16, y=1)
      current_time.after(1000, timer)

timer()

def location():
 timers_location = ttk.Label(window, text='Time, Karachi')
 timers_location.pack()
 timers_location.place(x=5, y=20)

location()

lable = ttk.Label(window, text="hour")
lable.pack()
lable.place(x=153, y=69)

hour= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# x = column and y = row
hour.pack(padx=10, pady=10)
hour.place(x=150, y=89)

lable = ttk.Label(window, text="minute")
lable.pack()
lable.place(x=217, y=69)

minute= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# x = column and y = row
minute.pack(padx=10, pady=10)
minute.place(x=220, y=89)

lable = ttk.Label(window, text="second")
lable.pack()
lable.place(x=287, y=69)

second= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# x = column and y = row
second.pack(padx=10, pady=10)
second.place(x=290, y=89)

pygame.mixer.init()

def play_sound():
  pygame.mixer.music.load("alarmtone.wav")
  pygame.mixer.music.play(loops=2)

def Cancel():
        window.destroy()

def what_button_will_do():
          while True:
            if hour.get() == '1':
              window.after(3600000, lambda : play_sound())

            if minute.get() == '1':
              window.after(60000, lambda : play_sound())

            if second.get() == '1':
              window.after(1900, lambda : play_sound())

            if hour.get() == '2':
              window.after(2*3600000, lambda : play_sound())

            if minute.get() == '2':
              window.after(2*60000, lambda : play_sound())

            if second.get() == '2':
              window.after(2*1000, lambda : play_sound())

            if hour.get() == '3':
              window.after(3*3600000, lambda : play_sound())

            if minute.get() == '3':
              window.after(3*60000, lambda : play_sound())

            if second.get() == '3':
              window.after(3*1000, lambda : play_sound())

            if hour.get() == '4':
              window.after(4*3600000, lambda : play_sound())

            if minute.get() == '4':
              window.after(4*60000, lambda : play_sound())

            if second.get() == '4':
              window.after(4*1000, lambda : play_sound())

            if hour.get() == '5':
              window.after(5*3600000, lambda : play_sound())

            if minute.get() == '5':
              window.after(5*60000, lambda : play_sound())

            if second.get() == '5':
              window.after(5*1000, lambda : play_sound())

            if hour.get() == '6':
              window.after(6*3600000, lambda : play_sound())

            if minute.get() == '6':
              window.after(6*60000, lambda : play_sound())

            if second.get() == '6':
              window.after(6*1000, lambda : play_sound())

            if hour.get() == '7':
              window.after(7*3600000, lambda : play_sound())

            if minute.get() == '7':
              window.after(7*60000, lambda : play_sound())

            if second.get() == '7':
              window.after(7*1000, lambda : play_sound())

            if hour.get() == '8':
              window.after(8*3600000, lambda : play_sound())

            if minute.get() == '8':
              window.after(8*60000, lambda : play_sound())

            if second.get() == '8':
              window.after(8*1000, lambda : play_sound())

            if hour.get() == '9':
              window.after(9*3600000, lambda : play_sound())

            if minute.get() == '9':
              window.after(9*60000, lambda : play_sound())

            if second.get() == '9':
              window.after(9*1000, lambda : play_sound())

            if hour.get() == '10':
              window.after(10*3600000, lambda : play_sound())

            if minute.get() == '10':
              window.after(10*60000, lambda : play_sound())

            if second.get() == '10':
              window.after(10*1000, lambda : play_sound())

            if hour.get() == '11':
              window.after(11*3600000, lambda : play_sound())

            if minute.get() == '11':
              window.after(11*60000, lambda : play_sound())

            if second.get() == '11':
              window.after(11*1000, lambda : play_sound())

            if hour.get() == '12':
              window.after(12*3600000, lambda : play_sound())

            if minute.get() == '12':
              window.after(12*60000, lambda : play_sound())

            if second.get() == '12':
              window.after(12*1000, lambda : play_sound())

            if hour.get() == '13':
              window.after(13*600000, lambda : play_sound())

            if minute.get() == '13':
              window.after(13*60000, lambda : play_sound())

            if second.get() == '13':
              window.after(13*1000, lambda : play_sound())

            if hour.get() == '14':
              window.after(14*3600000, lambda : play_sound())

            if minute.get() == '14':
              window.after(14*60000, lambda : play_sound())

            if second.get() == '14':
              window.after(14*1000, lambda : play_sound())

            if hour.get() == '15':
              window.after(15*3600000, lambda : play_sound())

            if minute.get() == '15':
              window.after(15*60000, lambda : play_sound())

            if second.get() == '15':
              window.after(15*1000, lambda : play_sound())

            if hour.get() == '16':
              window.after(16*3600000, lambda : play_sound())

            if minute.get() == '16':
              window.after(16*60000, lambda : play_sound())

            if second.get() == '16':
              window.after(16*1000, lambda : play_sound())

            if hour.get() == '17':
              window.after(17*3600000, lambda : play_sound())

            if minute.get() == '17':
              window.after(17*60000, lambda : play_sound())

            if second.get() == '17':
              window.after(17*1000, lambda : play_sound())

            if hour.get() == '18':
              window.after(18*3600000, lambda : play_sound())

            if minute.get() == '18':
              window.after(18*60000, lambda : play_sound())

            if second.get() == '18':
              window.after(18*1000, lambda : play_sound())

            if hour.get() == '19':
              window.after(19*3600000, lambda : play_sound())

            if minute.get() == '19':
              window.after(19*60000, lambda : play_sound())

            if second.get() == '19':
              window.after(19*1000, lambda : play_sound())

            if hour.get() == '20':
              window.after(20*3600000, lambda : play_sound())

            if minute.get() == '20':
              window.after(20*60000, lambda : play_sound())

            if second.get() == '20':
              window.after(20*1000, lambda : play_sound())

            if hour.get() == '21':
              window.after(21*3600000, lambda : play_sound())

            if minute.get() == '21':
              window.after(21*60000, lambda : play_sound())

            if second.get() == '21':
              window.after(21*1000, lambda : play_sound())

            if hour.get() == '22':
              window.after(22*3600000, lambda : play_sound())

            if minute.get() == '22':
              window.after(22*60000, lambda : play_sound())

            if second.get() == '22':
              window.after(22*1000, lambda : play_sound())

            if hour.get() == '23':
              window.after(23*3600000, lambda : play_sound())

            if minute.get() == '23':
              window.after(23*60000, lambda : play_sound())

            if second.get() == '23':
              window.after(23*1000, lambda : play_sound())

            if hour.get() == '24':
              window.after(24*3600000, lambda : play_sound())

            if minute.get() == '24':
              window.after(24*60000, lambda : play_sound())

            if second.get() == '24':
              window.after(24*1000, lambda : play_sound())

            if minute.get() == '25':
              window.after(25*60000, lambda : play_sound())

            if second.get() == '25':
              window.after(25*1000, lambda : play_sound())

            if minute.get() == '26':
              window.after(26*60000, lambda : play_sound())

            if second.get() == '26':
              window.after(26*1000, lambda : play_sound())

            if minute.get() == '27':
              window.after(27*60000, lambda : play_sound())

            if second.get() == '27':
              window.after(27*1000, lambda : play_sound())

            if minute.get() == '28':
              window.after(28*60000, lambda : play_sound())

            if second.get() == '28':
              window.after(28*1000, lambda : play_sound())

            if minute.get() == '29':
              window.after(29*60000, lambda : play_sound())

            if second.get() == '29':
              window.after(29*1000, lambda : play_sound())

            if minute.get() == '30':
              window.after(30*60000, lambda : play_sound())

            if second.get() == '30':
              window.after(30*1000, lambda : play_sound())

            if minute.get() == '31':
              window.after(31*60000, lambda : play_sound())

            if second.get() == '31':
              window.after(31*1000, lambda : play_sound())

            if minute.get() == '32':
              window.after(32*60000, lambda : play_sound())

            if second.get() == '32':
              window.after(32*1000, lambda : play_sound())

            if minute.get() == '33':
              window.after(33*60000, lambda : play_sound())

            if second.get() == '33':
              window.after(33*1000, lambda : play_sound())

            if minute.get() == '34':
              window.after(34*60000, lambda : play_sound())

            if second.get() == '34':
              window.after(34*1000, lambda : play_sound())

            if minute.get() == '35':
              window.after(35*60000, lambda : play_sound())

            if second.get() == '35':
              window.after(35*1000, lambda : play_sound())

            if minute.get() == '36':
              window.after(36*60000, lambda : play_sound())

            if second.get() == '36':
              window.after(36*1000, lambda : play_sound())

            if minute.get() == '37':
              window.after(37*60000, lambda : play_sound())

            if second.get() == '37':
              window.after(37*1000, lambda : play_sound())

            if minute.get() == '38':
              window.after(38*60000, lambda : play_sound())

            if second.get() == '38':
              window.after(38*1000, lambda : play_sound())

            if minute.get() == '39':
              window.after(39*60000, lambda : play_sound())

            if second.get() == '39':
              window.after(39*1000, lambda : play_sound())

            if minute.get() == '40':
              window.after(40*60000, lambda : play_sound())

            if second.get() == '40':
              window.after(40*1000, lambda : play_sound())

            if minute.get() == '41':
              window.after(41*60000, lambda : play_sound())

            if second.get() == '41':
              window.after(41*1000, lambda : play_sound())

            if minute.get() == '42':
              window.after(42*60000, lambda : play_sound())

            if second.get() == '42':
              window.after(42*1000, lambda : play_sound())

            if minute.get() == '43':
              window.after(43*60000, lambda : play_sound())

            if second.get() == '43':
              window.after(43*1000, lambda : play_sound())

            if minute.get() == '44':
              window.after(44*60000, lambda : play_sound())

            if second.get() == '44':
              window.after(44*1000, lambda : play_sound())

            if minute.get() == '45':
              window.after(45*60000, lambda : play_sound())

            if second.get() == '45':
              window.after(45*1000, lambda : play_sound())

            if minute.get() == '46':
              window.after(46*60000, lambda : play_sound())

            if second.get() == '46':
              window.after(46*1000, lambda : play_sound())

            if minute.get() == '47':
              window.after(47*60000, lambda : play_sound())

            if second.get() == '47':
              window.after(47*1000, lambda : play_sound())

            if minute.get() == '48':
              window.after(48*60000, lambda : play_sound())

            if second.get() == '48':
              window.after(48*1000, lambda : play_sound())

            if minute.get() == '49':
              window.after(49*60000, lambda : play_sound())

            if minute.get() == '49':
              window.after(49*1000, lambda : play_sound())

            if minute.get() == '50':
              window.after(50*60000, lambda : play_sound())

            if second.get() == '50':
              window.after(50*1000, lambda : play_sound())

            if second.get() == '51':
              window.after(3600000, lambda : play_sound())
              
            if minute.get() == '51':
              window.after(51*1000, lambda : play_sound())

            if minute.get() == '52':
              window.after(52*60000, lambda : play_sound())

            if second.get() == '52':
              window.after(52*1000, lambda : play_sound())

            if minute.get() == '53':
              window.after(53*60000, lambda : play_sound())

            if second.get() == '53':
              window.after(53*1000, lambda : play_sound())

            if minute.get() == '54':
              window.after(54*60000, lambda : play_sound())

            if second.get() == '54':
              window.after(54*1000, lambda : play_sound())

            if minute.get() == '55':
              window.after(55*60000, lambda : play_sound())

            if second.get() == '55':
              window.after(55*1000, lambda : play_sound())

            if minute.get() == '56':
              window.after(56*60000, lambda : play_sound())

            if second.get() == '56':
              window.after(56*1000, lambda : play_sound())

            if minute.get() == '57':
              window.after(57*60000, lambda : play_sound())

            if second.get() == '57':
              window.after(57*1000, lambda : play_sound())

            if minute.get() == '58':
              window.after(58*60000, lambda : play_sound())

            if second.get() == '58':
              window.after(58*1000, lambda : play_sound())

            if minute.get() == '59':
              window.after(59*60000, lambda : play_sound())

            if second.get() == '59':
              window.after(59*1000, lambda : play_sound())

            if minute.get() == '60':
              window.after(60*60000, lambda : play_sound())

            if second.get() == '60':
              window.after(60*1000, lambda : play_sound())

            if hour.get() == non_sense_input:
              _show("SetTimer", "Please enter an invalid value!")

            if minute.get() == non_sense_input:
              _show("SetTimer", "Please enter an invalid value!")

            if second.get() == non_sense_input:
              _show("SetTimer", "Please enter an invalid value!")

            if hour.get() == '' and minute.get() == '' and second.get() == '':
              _show("SetTimer", "Please enter an invalid value!")

            hour.delete(0, END)
            minute.delete(0, END)
            second.delete(0, END)

            break

non_sense_input = ('0' or '00')

button = ttk.Button(window, text='Set timer', command=what_button_will_do)
button.pack()
button.place(x=200, y=150)

secondbutton = ttk.Button(window, text='Cancel', width=6, command=Cancel)
secondbutton.pack()
secondbutton.place(x=430, y=290)

window.mainloop()