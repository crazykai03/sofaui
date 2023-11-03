# Import module
from tkinter import *
from PIL import ImageTk , Image
import threading
import time
lock_press_time =0
lock_hold= False
hold_time =0
hold_status= False
held_status = False
lock_state = True
pre_function_time =0
rf_tran_data = ""
command =[ord("B"),ord("E"),ord("2"),ord("1"),0]



def uppress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(up_btn, image = up_tap)



def uprelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(up_btn, image=up)
    command[4] = 0x01



def downpress(event):
        global pre_function_time
        pre_function_time = time.time()
        canvas1.itemconfig(down_btn, image=down_tap)


def downrelease(event):
        global pre_function_time
        pre_function_time = time.time()
        canvas1.itemconfig(down_btn, image=down)
        command[4] = 0x02


def stoppress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(stop_btn, image = stop_tap)
    command[4] = 0x03

def stoprelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(stop_btn, image=stop)



def lockpress(event):
    global  button1 ,lock_press_time , lock_hold , lock_state
    lock_hold = True
    canvas1.itemconfig(lock_btn, image = lock_tap)
    lock_state = True
    lock_press_time= time.time()
def lockrelease(event):
    global btn1 , lock_press_time , lock_hold ,lock_state
    lock_hold = False
    print(time.time()-lock_press_time)
    if (lock_state==True):
        canvas1.itemconfig(lock_btn, image=lock)

        unbind_btn()


def light1press(event):
    global pre_function_time,hold_status,hold_time
    pre_function_time = time.time()
    canvas1.itemconfig(light1_btn, image = light1_tap)
    hold_status = True
    command[4] = 0x80
    hold_time = time.time()


def light1release(event):
    global pre_function_time,hold_status,held_status
    pre_function_time = time.time()
    canvas1.itemconfig(light1_btn, image=light1)
    if held_status!=True:
        command[4] = 0xA8
    else:
        command[4] = 0x8A
    hold_status = False
    held_status = False


def light2press(event):
    global pre_function_time,hold_status,hold_time
    pre_function_time = time.time()
    canvas1.itemconfig(light2_btn, image = light2_tap)
    hold_status = True
    command[4] = 0x81
    hold_time = time.time()


def light2release(event):
    global pre_function_time,hold_status,held_status

    pre_function_time = time.time()
    canvas1.itemconfig(light2_btn, image=light2)
    if held_status != True:
        command[4] = 0xA9
    else:
        command[4] = 0x8B
    hold_status = False
    held_status = False

def light3press(event):
    global pre_function_time,hold_status,hold_time
    pre_function_time = time.time()
    canvas1.itemconfig(light3_btn, image = sofa_tap)
    hold_status = True
    command[4] = 0x82
    hold_time = time.time()


def light3release(event):
    global pre_function_time,hold_status,held_status

    pre_function_time = time.time()
    canvas1.itemconfig(light3_btn, image=sofa)
    if held_status != True:
        command[4] = 0xAA
    else:
        command[4] = 0x8C
    hold_status = False
    held_status = False

def alllightpress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(all_light_btn, image = all_light_tap)


def alllightrelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(all_light_btn, image=all_light)
    command[4] = 0xD7

def rgbpress(event):
    global pre_function_time,hold_status,hold_time
    pre_function_time = time.time()
    canvas1.itemconfig(rgb1_btn, image = dimming_tap)
    hold_status = True
    command[4] = 0xCB
    hold_time = time.time()


def rgbrelease(event):
    global pre_function_time,hold_status,held_status

    pre_function_time = time.time()
    canvas1.itemconfig(rgb1_btn, image=dimming)
    if held_status != True:
        command[4] = 0xC6
    else:
        command[4] = 0xD0
    hold_status = False
    held_status = False






#---------canvas 2















def serial_write():
    global  command
    print(command)
    print(bytes(command))











def mylog():
    global  lock_press_time , lock_state , pre_function_time,held_status
    if (time.time() - lock_press_time >=2 and lock_hold==True):
        canvas1.itemconfig(lock_btn, image=unlock)
        bind_btn()
        lock_state = False
        pre_function_time = time.time()
    elif (time.time() - pre_function_time >=30  and lock_state == False ):
        canvas1.itemconfig(lock_btn, image=lock)
        lock_state = True

        unbind_btn()

    if hold_status==True and time.time() - hold_time >=0.5 :
        held_status = True
        serial_write()
    elif  command[4] !=0x00 and hold_status==False:
        serial_write()
        command[4]=0x00




    threading.Timer(0.3, mylog).start()

def unbind_btn():
    canvas1.tag_unbind(up_btn, '<Button-1>' )
    canvas1.tag_unbind(up_btn, '<ButtonRelease-1>' )

    canvas1.tag_unbind(down_btn, '<Button-1>', )
    canvas1.tag_unbind(down_btn, '<ButtonRelease-1>' )

    canvas1.tag_unbind(stop_btn, '<Button-1>', )
    canvas1.tag_unbind(stop_btn, '<ButtonRelease-1>' )


    canvas1.tag_unbind(light1_btn, '<Button-1>' )
    canvas1.tag_unbind(light1_btn, '<ButtonRelease-1>' )

    canvas1.tag_unbind(light2_btn, '<Button-1>' )
    canvas1.tag_unbind(light2_btn, '<ButtonRelease-1>' )

    canvas1.tag_unbind(light3_btn, '<Button-1>' )
    canvas1.tag_unbind(light3_btn, '<ButtonRelease-1>')

    canvas1.tag_unbind(all_light_btn, '<Button-1>' )
    canvas1.tag_unbind(all_light_btn, '<ButtonRelease-1>' )

    canvas1.tag_unbind(rgb1_btn, '<Button-1>' )
    canvas1.tag_unbind(rgb1_btn, '<ButtonRelease-1>')





def bind_btn():
    canvas1.tag_bind(up_btn, '<Button-1>', uppress)
    canvas1.tag_bind(up_btn, '<ButtonRelease-1>', uprelease)

    canvas1.tag_bind(down_btn, '<Button-1>', downpress)
    canvas1.tag_bind(down_btn, '<ButtonRelease-1>', downrelease)

    canvas1.tag_bind(stop_btn, '<Button-1>', stoppress)
    canvas1.tag_bind(stop_btn, '<ButtonRelease-1>', stoprelease)

    canvas1.tag_bind(lock_btn, '<Button-1>', lockpress)
    canvas1.tag_bind(lock_btn, '<ButtonRelease-1>', lockrelease)

    canvas1.tag_bind(light1_btn, '<Button-1>', light1press)
    canvas1.tag_bind(light1_btn, '<ButtonRelease-1>', light1release)

    canvas1.tag_bind(light2_btn, '<Button-1>', light2press)
    canvas1.tag_bind(light2_btn, '<ButtonRelease-1>', light2release)

    canvas1.tag_bind(light3_btn, '<Button-1>', light3press)
    canvas1.tag_bind(light3_btn, '<ButtonRelease-1>', light3release)

    canvas1.tag_bind(all_light_btn, '<Button-1>', alllightpress)
    canvas1.tag_bind(all_light_btn, '<ButtonRelease-1>', alllightrelease)

    canvas1.tag_bind(rgb1_btn, '<Button-1>', rgbpress)
    canvas1.tag_bind(rgb1_btn, '<ButtonRelease-1>', rgbrelease)








# Create object
root = Tk()

# Adjust size
root.geometry("800x480")

# Add image file
bg = PhotoImage(file="Bg.png")
logo = PhotoImage(file="Logo.png")
up= PhotoImage(file="bed-default.png")
down= PhotoImage(file="party-tap.png")
stop = PhotoImage(file="stop-default.png")
light1= PhotoImage(file="light1-default.png")
light2= PhotoImage(file="light2-default.png")
sofa= PhotoImage(file="sofa-default.png")
dimming= PhotoImage(file="control-default.png")
all_light = PhotoImage(file="allLight-default.png")
#pop_up_bg = PhotoImage(file="Popup-Bg.png")
#change =  PhotoImage(file="change_btn.png")
#confirm =  PhotoImage(file="confirm_btn.png")
lock= PhotoImage(file="lock-default.png")
unlock = PhotoImage(file="unlock-default.png")
#option = PhotoImage(file="option.png")
#------------for tap button--------------------------------

up_tap= PhotoImage(file="bed-tap.png")
down_tap= PhotoImage(file="party-default.png")
stop_tap = PhotoImage(file="stop-tap.png")
light1_tap= PhotoImage(file="light1-tap.png")
light2_tap= PhotoImage(file="light2-tap.png")
sofa_tap= PhotoImage(file="sofa-tap.png")
dimming_tap= PhotoImage(file="control-tap.png")
all_light_tap = PhotoImage(file="allLight-tap.png")
lock_tap= PhotoImage(file="lock-tap.png")
unlock_tap= PhotoImage(file = "unlock-tap.png")
#change_tap =  PhotoImage(file="change_tap.png")
#confirm_tap =  PhotoImage(file="confirm_tap.png")
#all_dark = PhotoImage(file = "all_dark_bg.png")







# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=480,bd=0, highlightthickness=0 , bg="#2B2E35")
canvas2 = Canvas(root, width=800,
                 height=480,bd=0, highlightthickness=0 , bg="#2B2E35")
canvas1.pack(fill="both", expand=True)


# Display image
#canvas1.create_image(0, 0, image=bg,anchor="nw")






offset_x = 72
offset_y = 87



# Display Buttons
bg_img_all = canvas1.create_image(400,240,image=bg)
logo_btn = canvas1.create_image(24+186,24+28,image=logo)
up_btn = canvas1.create_image(24+offset_x,100+offset_y,image=up)
down_btn = canvas1.create_image(326+offset_x,100+offset_y,image=down)
stop_btn =  canvas1.create_image(24+148,282+87,image=stop)
lock_btn =  canvas1.create_image(326+offset_x,282+offset_y,image=lock)

light1_btn =  canvas1.create_image(480+72,100+42,image=light1)
light2_btn =  canvas1.create_image(480+72,191+42,image=light2)
light3_btn =  canvas1.create_image(160+offset_y,100+offset_y,image=sofa)
rgb1_btn =  canvas1.create_image(616+offset_y,100+offset_y,image=dimming)
all_light_btn =  canvas1.create_image(480+148,282+87,image=all_light)
#option_btn =  canvas1.create_image(480+offset_y,185+offset_y,image=option)




#------canvas 2 -----------------
#bg_img_dark = canvas2.create_image(400,240,image=all_dark)
#pop_up_background =  canvas2.create_image(176+224,16+224,image=pop_up_bg)
#change_btn =  canvas2.create_image(400,220,image=change)
#confirm_btn =  canvas2.create_image(400,220+170,image=confirm)




bind_btn()
unbind_btn()










#canvas1.itemconfig(lock,state='hidden')






mylog()


# Execute tkinter

root.overrideredirect(True)

root.mainloop()