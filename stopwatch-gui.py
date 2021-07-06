import tkinter as tk  
from datetime import datetime 
counter = 66600
running = False
def counter_label(wel_label):  
    def count():  
        if running:  
            global counter  
            if counter==66600:              
                display="Starting..."
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%H:%M:%S") 
                display=string  
    
            wel_label['text']=display  
            wel_label.after(1000, count)   
            counter += 1  
    count()  
def Start(wel_label):  
    global running  
    running=True
    counter_label(wel_label)  
    Time_Start['state']='disabled'
    Time_Stop['state']='normal'
    Time_Reset['state']='normal'  
def Stop():  
    global running  
    Time_Start['state']='normal'
    Time_Stop['state']='disabled'
    Time_Reset['state']='normal'
    running = False  
def Reset(wel_label):  
    global counter 
    counter=66600  
    if running==False:        
        Time_Reset['state']='disabled'
        wel_label['text']='Welcome!'  
    else:                 
        wel_label['text']='Starting the Time'
root = tk.Tk()  
root.title("Gui-Stopwatch")  
root.minsize(width=600, height=600)
root['bg']='Black'
wel_label = tk.Label(root, text="Welcome!", fg="Pink",bg="Black", font=("Comic Sans Ms", 60 ))  
wel_label.pack()
frame = tk.Frame(root) 
Time_Start = tk.Button(frame, text='Start', width=6,bg="Dark Green",fg='White', command=lambda:Start(wel_label),font=("Comic Sans Ms", 30 ))  
Time_Stop = tk.Button(frame, text='Stop',bg="Red",fg='White' , width=6,state='disabled', command=Stop,font=("Comic Sans Ms", 30)) 
Time_Reset = tk.Button(frame, text='Reset',bg="Yellow",fg='Black' , width=6, state='disabled', command=lambda:Reset(wel_label),font=("Comic Sans Ms", 30))  
frame.pack(anchor = 'center',pady=5) 
Time_Start.pack(side="left")  
Time_Stop.pack(side ="left")  
Time_Reset.pack(side="left")  
root.mainloop()
