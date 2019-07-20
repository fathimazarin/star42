from Tkinter import *
from implibs import *
#from mainprgm import *
from PIL import Image, ImageTk
#from mainprgm import *

def ResWin():
    m=Tk()

#self.init_window()
    m.title("Find out the constellation!")
        #self.pack(fill=BOTH, expand=1)
    return_button=Button(m,text="Return to Home page",command= lambda: Homepage(Tk())).grid(row=3,column=1)
    close_button = Button(m, text="Close", command=m.quit)
    another_button=Button(m,text="Check another image",command= lambda: insertimg(Tk())).grid(row=2,column=1)
    close_button.grid(row=4,column=1)
    r=np.zeros((4,1),dtype=int)
        #r=result
    i=0
    photo_image=[]
    for name in const_name:
        load=Image.open("Desktop/guistuff/"+name+".jpg")
        load = load.resize((250, 250), Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        photo_image.append(render)
        img=Label(m,image=render).grid(row=0,column=i)
        nm=''.join(map(str,r[i]))
        w=Label(m,text=const_name[i]+":"+nm,fg="red").grid(row=1,column=i)
        i=i+1
    m.mainloop()

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
#m=Tk()
#app=ResWin(m)
#ResWin(Tk()).mainloop()
ResWin()
