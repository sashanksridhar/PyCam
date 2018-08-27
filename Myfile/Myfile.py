import sys
import cv2
import time
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import tkinter as tk
import PIL.Image
import PIL.ImageTk
import Myfile_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    Myfile_support.init(root, top)
    root.mainloop()
    

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    Myfile_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        self.flag = 0
        self.flag1 = 0
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.vs = cv2.VideoCapture(0)
        self.vs.set(3,640)
        self.vs.set(4,480)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('E:\Pictures\output.avi',self.fourcc, 20.0, (640,480))        
        self.Button1 = Button(top,command=self.buttonClick)
        self.Button1.place(relx=0.12, rely=0.71, height=33, width=206)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Take Photo''')
        self.Button1.configure(width=206)

        self.Button2 = Button(top,command = self.videorecord)
        self.Button2.place(relx=0.6, rely=0.71, height=33, width=186)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Take Video''')
        self.Button2.configure(width=186)

        self.Frame1 = Frame(top,)
        self.Frame1.place(relx=0.12, rely=0.04, relheight=0.59, relwidth=0.78)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=465)
        
        self.Button3 = Button(top,command = self.stoprecord)
        self.Button3.place(relx=0.4, rely=0.87, height=33, width=156)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Stop Video''')
        self.Button3.configure(width=156)        
        
        
        
        self.lmain = tk.Label(self.Frame1)
        self.lmain.grid(row=0, column=0)
        
        self.video_loop()
        
    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        if(self.flag):
            return
        ok, frame = self.vs.read()  # read frame from video stream
          # frame captured without any errors
        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert colors from BGR to RGBA
        self.img = frame
        self.current_image = PIL.Image.fromarray(cv2image)  # convert image for PIL
        
        
        self.current_image = self.current_image.resize((self.Frame1.winfo_pixels(self.Frame1.winfo_width()), self.Frame1.winfo_pixels(self.Frame1.winfo_width())), PIL.Image.ANTIALIAS)
        imgtk = PIL.ImageTk.PhotoImage(image=self.current_image)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        
        self.lmain.after(10, self.video_loop) 
    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        cv2.imwrite('E:\Pictures\photo.jpg',self.img)        
    def videorecord(self):
        self.flag = 1
        #self.vs.release()
        #cv2.destroyAllWindows()
        #self.vs.open(0)
        if(self.flag1):
            self.flag = 0
            self.out.release()
            return
        
        ok, frame = self.vs.read()  # read frame from video stream
        # frame captured without any errors

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert colors from BGR to RGBA
        self.img = frame
        self.current_image = PIL.Image.fromarray(cv2image)  # convert image for PIL


        self.current_image = self.current_image.resize((self.Frame1.winfo_pixels(self.Frame1.winfo_width()), self.Frame1.winfo_pixels(self.Frame1.winfo_width())), PIL.Image.ANTIALIAS)
        imgtk = PIL.ImageTk.PhotoImage(image=self.current_image)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.out.write(self.img)
        self.lmain.after(10, self.videorecord)   
            
    def stoprecord(self):
        self.flag1 = 1
        self.lmain.after(10,self.video_loop)

if __name__ == '__main__':
    vp_start_gui()
    