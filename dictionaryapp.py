#!/usr/bin/env python

import tkinter as tk
from PIL import Image, ImageTk
import requests # needed for API requests
from tkinter import font

# **** functions for gui, always above gui layout *****
def test_function(entry):
    print("This is the entry:", entry)

def format_response(lookup):
    try:
        word = lookup['results'][0]['id']
        wordtype = lookup['results'][0]['lexicalEntries'][0]['lexicalCategory']['id']
        defin = lookup['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        final_str = "Word: %s \nType: %s \nDefinition: %s." % (word, wordtype, defin)
    except:  
        final_str = 'There was a problem retrieving that information. \n Please try searching for another word.'
    
    return final_str

def get_defintion(word_id):
    app_id = 'your api id'
    app_key = 'your api key'
    endpoint = "entries"
    language_code = "en-us"
    fields = 'definitions'
    strictMatch = 'false'
    url = "https://od-api.oxforddictionaries.com/api/v2/"+ endpoint+"/"+language_code+"/"+word_id  + '?fields=' + fields + '&strictMatch=' + strictMatch;
    headers = {"app_id": app_id, "app_key": app_key,"word_id":word_id, 'units': 'imperial'}
    response = requests.get(url, headers=headers)
    lookup = response.json()
    #print(response.json()) # testing
    label['text'] = format_response(lookup)
    

    # *** Setup for Gui ****
root = tk.Tk()
root.title("Dictionary App")

# *** pre defined height and width *****
win_height = 100
win_width = 100
root.resizable(False,False)
root.configure(background="black")


canvas = tk.Canvas(root, height=win_height, width=win_width)
canvas.pack()

load = Image.open('the image to your background photo')
render = ImageTk.PhotoImage(load)
img = tk.Label(canvas, image=render)
img.pack(fill='both')


frame = tk.Frame(root, bg='#000000', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') #fills frame

banner = tk.Label(canvas, text="Dictionary App : Written by Christopher Durham Jr. : Powered by Oxford", bg="black", foreground="white")
banner.pack(fill='both')

entry = tk.Entry(frame, font=('Chilanka', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text= "Search",font=('Chilanka', 15) ,command=lambda: get_defintion(entry.get()))  #lamda used to define code in real time
button.place(relx=0.7,relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#000000', bd=9)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Chilanka', 18), anchor='nw', justify='left', bd=4, wraplength=350)
label.place(relwidth=1, relheight=1)



root.mainloop()
