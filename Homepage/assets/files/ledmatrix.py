import time, os

from sense_hat import SenseHat

sense=SenseHat()

g=[0,255,0]
r=[255,0,0]
e=[0,0,0]

icon_finish = [
e,e,e,r,r,e,e,e,
e,e,r,e,e,r,e,e,
e,r,e,e,e,e,r,e,
r,e,e,r,r,e,e,r,
r,e,e,r,r,e,e,r,
e,r,e,e,e,e,r,e,
e,e,r,e,e,r,e,e,
e,e,e,r,r,e,e,e,
]

icon_arrow =[
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
]

def display_letter(text,txt_colour,bg_color):
    if bg_color=="":
        bg_color = [255,255,255]
    if txt_colour=="":
        txt_colour=[0,0,0]

    text=str(text)

    sense.show_letter(text,text_colour=txt_colour,\
                      back_colour=bg_color)
    return -1

def display_message(text,txt_colour,bg_color,speed):
    if bg_color=="":
        bg_color=[255,255,255]
    if txt_colour=="":
        txt_colour=[0,0,0]

    text=str(text)
    sense.show_message(text,scroll_speed=speed, \
                       text_colour=txt_colour,back_colour=bg_color)
    return -1

def display_pixels(icon):
    if icon =="arrow":
        sense.set_pixels(icon_arrow)
    elif icon=="finish":
        sense.set_pixels(icon_finish)
    return -1

def display_rotate(value):
    if value==0:
        sense.set_rotation(value)
    elif value==90:
        sense.set_rotation(value)
    elif value==180:
        sense.set_rotation(value)
    elif value==270:
        sense.set_rotation(value)
    return -1

def display_image(file_path):
    if os.path.isfile(file_path)==True:
        sense.load_image(file_path,redraw=True)
    return -1

def display_clear():
    sense.clear(255,255,255)
    return -1

def display_flip(flip):
    if flip=="h":
        sense.flip_h()
    return -1
    