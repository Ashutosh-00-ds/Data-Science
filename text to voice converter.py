#3.10.4
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pyttsx3

def convert():
    engine = pyttsx3.init()
    engine.setProperty('volume', volume_var.get() / 100)  # Set volume based on the volume scale value
    engine.setProperty('rate', speed_var.get())  # Set speech rate based on the speed scale value

    voices = engine.getProperty('voices') 
    gender = gender_var.get()  # Get selected gender (0 for male, 1 for female)
    if gender == 0:
        engine.setProperty('voice',voices[0].id )  # Set male voice
    elif gender == 1:
        engine.setProperty('voice', voices[1].id)  # Set female voice

    x = text_box.get(1.0, tk.END).strip()  # Get text from text box
    engine.say(x)
    engine.runAndWait()
   
def save_audio():
    engine = pyttsx3.init()
    engine.setProperty('volume', volume_var.get() / 100)  # Set volume based on the volume scale value
    engine.setProperty('rate', speed_var.get())  # Set speech rate based on the speed scale value

    gender = gender_var.get()  # Get selected gender (0 for male, 1 for female)
    if gender == 0:
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')  # Set male voice
    elif gender == 1:
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')  # Set female voice

    x = text_box.get(1.0, tk.END).strip()  # Get text from text box
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file:
        engine.save_to_file(x, output_file)
        engine.runAndWait()  

win = tk.Tk()
win.title(" Text To Voice Converter")
win.maxsize(width=700, height=700)
win.minsize(width=700, height=700)

#heading label
head_label = tk.Label(win, text='Text To Voice Converter', font=('Arial', 30, 'bold'), bd=10, relief=tk.GROOVE, bg='sky blue')
head_label.pack(fill='x')

#background
back = tk.Label(win, bg='gray', bd=10, relief=tk.GROOVE, height=400)
back.pack(fill='x')

#text label
text_label = tk.Label(back, text='Enter Text :', font=('Arial', 20, 'bold'), fg='black', bg='gray')
text_label.place(x=20, y=100)

# Text box
text_box = tk.Text(back, font=('arial', 13), bd=5, bg='gray')
text_box.place(x=200, y=80, width=350, height=100)

#convert button
convert_button = tk.Button(back, text='CONVERT', font=('arial', 10, 'bold'), bd=5, activebackground='blue', width=10, height=2, bg='gray', command=convert)
convert_button.place(x=200, y=480)

#save button
save_button = tk.Button(back, text='SAVE', font=('arial', 10, 'bold'), bd=5, activebackground='blue', width=10, height=2, bg='gray', command=save_audio)
save_button.place(x=350, y=480)

# Volume control
volume_label = tk.Label(back, text='Volume :', font=('Arial', 15, 'bold'), fg='black', bg='gray')
volume_label.place(x=150, y=280)
volume_var = tk.IntVar(value=100)  # Default volume value
volume_scale = tk.Scale(back, from_=0, to=100, orient=tk.HORIZONTAL, variable=volume_var,bg='gray')
volume_scale.place(x=270, y=280,width=200)

# Gender selection
gender_label = tk.Label(back, text='Gender :', font=('Arial', 17, 'bold'), fg='black', bg='gray')
gender_label.place(x=150, y=210)
gender_var = tk.IntVar(value=0)  # Default to male
male_radio = tk.Radiobutton(back, text="Male", variable=gender_var, value=0,bg='gray',font=('Arial', 15, 'bold'))
female_radio = tk.Radiobutton(back, text="Female", variable=gender_var, value=1,bg='gray',font=('Arial', 15, 'bold'))
male_radio.place(x=260, y=210)
female_radio.place(x=350, y=210)

# Speech speed control
speed_label = tk.Label(back, text='Speed : ', font=('Arial', 15, 'bold'), fg='black', bg='gray')
speed_label.place(x=150, y=350)
speed_var = tk.IntVar(value=200)  # Default speed value
speed_scale = tk.Scale(back, from_=50, to=300, orient=tk.HORIZONTAL, variable=speed_var,bg='gray')
speed_scale.place(x=270, y=350,width=200)

win.mainloop()
