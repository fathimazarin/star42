from tkinter import *
import os
import urllib.request as url
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import numpy as np
import webbrowser
import implibs


root = Tk()
root.geometry("1920x1080")
frame1 = Frame(root)
frame2 = Frame(root)
new = 1
url1= "https://github.com/fathimazarin/star42"
url2="https://docs.google.com/document/d/101hhSNMt-TyTPod5bsKhQ6MmauDPQBo36w2biU0HhA8/edit"
def openweb1():
	webbrowser.open(url1,new = new)

def openweb2():
	webbrowser.open(url2,new = new)

def run():
    webbrowser.get(using = 'windows-default').open("file:///D:/Documents/user-interface/star43/process.html")
    import mainprgm
    global results
    results = mainprgm.main(np.array(img))
    os.system("taskkill /im chrome.exe /f")
    button4.pack()

#################################
v = IntVar()
def openchecklist():
    button1.pack_forget()
    radiobutton1.pack(anchor = S)
    radiobutton2.pack(anchor = S)
    button2.pack(anchor = S)

def takeinput():
    txt.pack_forget()
    label99.pack_forget()
    label999.pack_forget()
    x = v.get()
    button2.pack_forget()
    if x == 1:
        radiobutton2.pack_forget()
        #global filename
        filename = askopenfilename()
        radiobutton1.pack_forget()
        label = Label(frame1,text = 'File: ' + filename)
        label.pack(anchor = NW)
        global img
        img = Image.open(filename)
        photo = ImageTk.PhotoImage(img)
        label1 = Label(frame1,image = photo)
        label1.image = photo
        label1.pack(anchor = S)


    if x == 2:
        radiobutton1.pack_forget()
        global entry1
        entry1 = Entry(frame1)
        entry1.bind('<Return>',sendinput)
        entry1.pack()

def sendinput(event):
    entry1.pack_forget()
    resource = url.urlopen(entry1.get())
    output = open('fileio.jpg','wb')
    output.write(resource.read())
    output.close()
    global img
    img = Image.open('fileio.jpg')
    photo = ImageTk.PhotoImage(img)
    label3 = Label(frame1,image = photo)
    label3.image = photo
    label3.pack()







#################################Z
def ResWin():
    frame1.pack_forget()
    frame2.pack()
    return_button=Button(frame2,text="Return to Home page",command= homepage).grid(row=2,column=1,columnspan = 2)
    close_button = Button(frame2, text="Close", command=root.destroy)
    close_button.grid(row=3,columnspan = 2,column = 1)
    r=results
    i=0
    photo_image=[]
    for name in implibs.const_name:
        load=Image.open("D:/Documents/user-interface/star43/"+ name +".jpg")
        load = load.resize((250, 250), Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        photo_image.append(render)
        img100=Label(frame2,image=render)
        img100.image = render
        img100.grid(row = 0,column = i)
        nm=''.join(map(str,r[i]))
        w=Label(frame2,text=implibs.const_name[i]+":"+nm,fg="red").grid(row=1,column=i)
        i=i+1
#################################Z
#################################I
def homepage():
	frame2.pack_forget()
	for widget in frame1.winfo_children():
		widget.pack_forget()
	frame1.pack()
	txt.pack()
	label99.pack()
	label999.pack()
	button1.pack()
#################################I
menu = Menu(root)
root.config(menu = menu)
subpre = Menu(menu)

menu.add_command(label='Run',command = run)
menu.add_command(label='Code',command = openweb1)
menu.add_command(label='Documentation',command = openweb2)

menu.add_cascade(label='Presentation',menu =subpre)
subpre.add_command(label='ppt')#,command=hello)
subpre.add_command(label='video')#,command=hello)

frame1.pack()
txt = Label(frame1,text = '\n\n\n\nWhen you randomly look at the night sky, ever wondered which consellation you were looking at?\n That can be quite hard to answer for someone who is not a seasoned stargazer. \n This application aims to bridge that gap between you and a seasoned stargazer.\n \n \n\n\n',font='Helvetica 10 bold')
txt.pack()
img99 = Image.open('out.png')
photo99 = ImageTk.PhotoImage(img99)
label99 = Label(frame1,image = photo99)
label99.image = photo99
label99.pack()
label999 = Label(frame1,text = '\n')
label999.pack()

button1 = Button(frame1,text = 'Select Input Type',command = openchecklist)
button1.pack()
button2 = Button(frame1,text = 'Next',command = takeinput)
radiobutton1 = Radiobutton(frame1,text = 'File',variable = v,value = 1)
radiobutton2 = Radiobutton(frame1,text = 'URL',variable = v,value = 2)
button4 = Button(frame1,text = 'Show Result',command = ResWin)
#################################


root.mainloop()
