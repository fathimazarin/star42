from Tkinter import *
from implibs import *
from mainprgm import *
from PIL import Image, ImageTk

#m=Tk()
#def combfns(*fn1):
 ########CONTAINS CLASS REPRESENTATION

class ResWin(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        #self.init_window()
        self.master.title("Find out the constellation!")
        #self.pack(fill=BOTH, expand=1)
        self.return_button=Button(self.master,text="Return to Home page",command= lambda: Homepage(Tk())).grid(row=3,column=1)
        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.another_button=Button(self.master,text="Check another image",command= lambda: insertimg(Tk())).grid(row=2,column=1)
        self.close_button.grid(row=4,column=1)
        #self.r=np.zeros((4,1),dtype=int)
        r=result
        i=0
        self.photo_image=[]
        for name in const_name:
            self.load=Image.open("Desktop/guistuff/"+name+".jpg")
            self.load = self.load.resize((250, 250), Image.ANTIALIAS)
            self.render=ImageTk.PhotoImage(self.load)
            self.photo_image.append(self.render)
            self.img=Label(self.master,image=self.render).grid(row=0,column=i)
            nm=''.join(map(str,self.r[i]))
            self.w=Label(self.master,text=const_name[i]+":"+nm,fg="red").grid(row=1,column=i)
            i=i+1

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
ResWin(Tk()).mainloop()
#app.mainloop()
