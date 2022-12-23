#Kanishk Jain
# SIT 210 - Final Project
#Ganga Info and Reserve System

from tkinter import * 
import pygame
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
import pyrebase
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import pyttsx3


engine = pyttsx3.init()

config = {
  "apiKey": "AIzaSyDMvKNQq0vFFXei9I-xFwHEsmG9yrjQtVA",
  "authDomain": "arduinonano-f0e48.firebaseapp.com",
  "databaseURL": "https://arduinonano-f0e48-default-rtdb.firebaseio.com",
  "storageBucket": "arduinonano-f0e48.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
head = db.child("mlx90614")

value_1 = head.child("phval").get().val()
value_2 = head.child("tds").get().val()

def getValues():
    value_1 = head.child("phval").get().val()
    value_2 = head.child("tds").get().val()
    header2.config(text = f"tds: {value_2}")
    header3.config(text = f"pH: {value_1}")
    root.after(3000, getValues)



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ganga_led = LED(14)
upper_led = LED(15)
middle_led = LED(18)

root = Tk()
root.title("Mountain Info System")
root.geometry('350x450')
root.configure(bg='#87CEEB')     #to set the background colour of the root

# Defining a font to use it for the button text (optional)
buttonFont = tkinter.font.Font(family="Helvetica", size= 12, weight="bold")
HeaderFont = tkinter.font.Font(family="Helvetica", size= 24, weight="bold")

#Label to show the header text  
header1= Label(root, text ="Ganga Info System", font= HeaderFont, bg='white', padx= 20)
header1.grid(row=0, column= 0)

header2= Label(root, text =f"tds: {value_2}", font= HeaderFont, bg='white', padx= 20)
header2.grid(row=1, column= 0)

header3= Label(root, text =f"Ph: {value_1}", font= HeaderFont, bg='white', padx= 20)
header3.grid(row=2, column= 0)


def lower():
  #pygame.mixer.music.load("1.mp3")
  #pygame.mixer.music.play(loops=0)
  ganga_led.off()
  middle_led.off()
  upper_led.off()
  engine.say("In between the Shiwaliks in the south and the Greater Himalayas in the nort runs almost parallel to both the ranges is called the Himachal or Lower Himalaya.Lower Himalayan ranges are 60-80 km wide and about 2400 km in length. Elevations vary from 3,500 to 4,500 m above sea level. Many peaks are more than 5,050 m above sea level and are snow covered throughout the year. Lower Himalayas have steep, bare southern slopes [steep slopes prevents soil formation] and more gentle, forest covered northern slopes. In Uttarakhand, the Middle Himalayas are marked by the Mussoorie and the Nag Tibba ranges.")
  engine.run()
  
def middle():
  #pygame.mixer.music.load("2.mp3")
  #pygame.mixer.music.play(loops=0)
  middle_led.on()
  upper_led.off()
  ganga_led.off()
  engine.say("Lesser Himalayas, also called Inner Himalayas, Lower Himalayas, or Middle Himalayas, middle section of the vast Himalayan mountain system in south-central Asia. The Lesser Himalayas extend for some 1,550 miles (2,500 km) northwest-southeast across the northern limit of the Indian subcontinent. Areas include the disputed Kashmir region (Gilgit-Baltistan, administered by Pakistan, and Jammu and Kashmir union territory, administered by India), the Indian states of Himachal Pradesh and Uttarakhand, Nepal, the Indian state of Sikkim, and Bhutan. The range lies between the Great Himalayas to the northeast and the Siwalik Range (Outer Himalayas) to the southeast and has an average elevation of 12,000 to 15,000 feet")
  engine.runAndWait()
  
def upper():
  #pygame.mixer.music.load("3.mp3")
  #pygame.mixer.music.play(loops=0)
  upper_led.on()
  middle_led.off()
  ganga_led.off()
  engine.say("The Great Himalaya Also known as Inner Himalaya, Central Himalaya or Himadri. Average elevation of 6,100 m above sea level and an average width of about 25 km. It is mainly formed of the central crystallines (granites and gneisses) overlain by metamorphosed sediments [limestone].The folds in this range are asymmetrical with steep south slope and gentle north slope giving ‘hog back (a long, steep hill or mountain ridge)’ topography. This mountain arc convexes to the south just like the other two. Terminates abruptly at the syntaxial bends. One in the Nanga Parbat in north-west and the other in the Namcha Barwa in the north-east. This mountain range boasts of the tallest peaks of the world, most of which remain under perpetual snow. ")
  engine.runAndWait()

def ganga_voice():
  #pygame.mixer.music.load("4.mp3")
  #pygame.mixer.music.play(loops=0)
  ganga_led.on()
  upper_led.off()
  middle_led.off()
  engine.say("The Ganges rises in the southern Great Himalayas, and its five headstreams—the Bhagirathi, the Alaknanda, the Mandakini, the Dhauliganga, and the Pindar—all rise in the mountainous region of northern Uttarakhand state. The two main headstreams are the Alaknanda and the Bhagirathi. The Ganges basin is one of the most densely populated regions on earth. The untreated sewage dumped into the river, industrial waste, agricultural runoff, remnants of partially burned or unburned bodies from funeral pyres, and animal carcasses all contribute to polluting the Ganges. High levels of disease-causing bacteria and toxic substances have also been found in the Ganges.In between the Shiwaliks in the south and the Greater Himalayas in the nort runs almost parallel to both the ranges is called the Himachal or Lower Himalaya. Lower Himalayan ranges are 60-80 km wide and about 2400 km in length. Elevations vary from 3,500 to 4,500 m above sea level. Many peaks are more than 5,050 m above sea level and are snow covered throughout the year. Lower Himalayas have steep, bare southern slopes [steep slopes prevents soil formation] and more gentle, forest covered northern slopes. In Uttarakhand, the Middle Himalayas are marked by the Mussoorie and the Nag Tibba ranges. ")
  engine.runAndWait()

lower_him = Button(root, text='Lower Himalayas', font= buttonFont, command= lower, bg= '#6495ED', height= 3, width= 15)
lower_him.grid(row= 4, column=0)

middle_him = Button(root, text='Middle Himalayas', font= buttonFont, command= middle, bg= '#87CEFA', height= 3, width= 15)
middle_him.grid(row= 5, column=0)

upper_him = Button(root, text='Upper Himalayas', font= buttonFont, command= upper, bg= '#E0FFFF', height= 3, width= 15)
upper_him.grid(row= 6, column=0)

ganga = Button(root, text='Ganga River', font= buttonFont, command= ganga_voice, bg= 'red', height= 3, width= 15)
ganga.grid(row= 7, column=0)

GPIO.cleanup()

root.after(3000, getValues)
root.mainloop()
