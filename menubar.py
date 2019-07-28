from tkinter import *
#import cv2
import os
import pickle
import urllib.request as url
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import numpy as np
import time
import threading
import webbrowser
import implibs


root = Tk()
root.geometry("1920x1080")
frame1 = Frame(root)
frame2 = Frame(root)
#v = IntVar()
new = 1
url1= "https://github.com/fathimazarin/star42"
url2="https://docs.google.com/document/d/101hhSNMt-TyTPod5bsKhQ6MmauDPQBo36w2biU0HhA8/edit"
def openweb1():
	webbrowser.open(url1,new = new)

def openweb2():
	webbrowser.open(url2,new = new)

def hello():
    print("hello!")

def takeinput1():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file loation on comp
	button1.pack_forget()
	filename='D:/Documents/geminitest1.png'
	global img
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(frame1,image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput2():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	button1.pack_forget()
	filename ='D:/Documents/geminitest1.png'
	global img
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(frame1,image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput3():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	button1.pack_forget()
	filename ='D:/Documents/geminitest1.png'
	global img
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(frame1,image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput4():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	button1.pack_forget()
	filename ='D:/Documents/geminitest1.png'
	global img
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(frame1,image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def run1():
    #t = threading.Thread(target = statusbar,args = ())
    #t.start()
    #while t.is_alive():
    webbrowser.get(using = 'windows-default').open("file:///D:/Documents/user-interface/star43/process.html")
    import mainprgm
    global results
    results = mainprgm.main(np.array(img))
    #print(results)
        #break
    #root.destroy()
    os.system("taskkill /im edge.exe /f")
    button4.pack()
    #ResWin()

'''def run2():
	p1 = Process(target = run1)
	p1.start()
	p2 = Process(target = statusbar)
	p2.start()
	p1.join()
	p2.join()'''
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
        #button3.pack()

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
    #button3.pack()



def run():
    #button3.pack_forget()
    t = threading.Thread(target = statusbar,args = ())
    t.start()
    global results
    while t.is_alive():
        import mainprgm
        results = mainprgm.main(np.array(img))
        break
    #root.destroy()
    button4.pack()
    #ResWin()


#################################Z
def ResWin():
    frame1.pack_forget()
    frame2.pack()
    #m=Tk()

#self.init_window()
    #m.title("Find out the constellation!")
        #self.pack(fill=BOTH, expand=1)
    return_button=Button(frame2,text="Return to Home page",command= homepage).grid(row=2,column=1,columnspan = 2)
    close_button = Button(frame2, text="Close", command=root.destroy)
    #another_button=Button(frame2,text="Check another image",command= lambda: insertimg(Tk())).grid(row=2,column=1)
    close_button.grid(row=3,columnspan = 2,column = 1)
    #r=np.zeros((4,1),dtype=int)
    r=results
    i=0
    photo_image=[]
    for name in implibs.const_name:
        load=Image.open("D:/Documents/user-interface/star43/"+ name +".jpg")
        load = load.resize((250, 250), Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        photo_image.append(render)
        img100=Label(frame2,image=render)#.grid(row=0,column=i)
        img100.image = render
        img100.grid(row = 0,column = i)
        nm=''.join(map(str,r[i]))
        w=Label(frame2,text=implibs.const_name[i]+":"+nm,fg="red").grid(row=1,column=i)
        i=i+1
    #m.mainloop()

class Homepage(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        #self.master=master
        self.master.title("Mock Home")
        #self.text=Label(self.master,text="mock homepage",fg="blue").grid(row=0,column=0)

class insertimg(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        #self.master=master
        self.master.title("Mock insert page")
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
#imgcon = Menu(menu)
subpre = Menu(menu)
#menu.add_command(label='Home',command=hello)

#menu.add_cascade(label='Images',menu=imgcon)
#imgcon.add_command(label='Gemini',command =takeinput1)

#imgcon.add_command(label='Cassiopia',command = takeinput2)
#imgcon.add_command(label='Orion',command = takeinput3)
#imgcon.add_command(label='Ursa Major',command = takeinput4)

menu.add_command(label='Run',command = run1)
menu.add_command(label='Code',command = openweb1)
menu.add_command(label='Documentation',command = openweb2)

menu.add_cascade(label='Presentation',menu =subpre)
subpre.add_command(label='ppt',command=hello)
subpre.add_command(label='vedio',command=hello)

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
#button3 = Button(root,text = 'Run',command = run)
button4 = Button(frame1,text = 'Show Result',command = ResWin)
#################################


root.mainloop()
