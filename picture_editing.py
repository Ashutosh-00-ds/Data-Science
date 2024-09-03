#3.10.4

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, colorchooser
import cv2
import numpy as np
from PIL import Image,ImageTk


#funcations
def load_image():
    path=filedialog.askopenfilename()
    if path:
        path_entry.delete(0,tk.END)
        path_entry.insert(0,path)
        global original_image
        original_image=cv2.imread(path)
        original_image=cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB) 
        show_original(original_image)
        
# funcation original image

# show original image
def show_original(image):
    if image is not None:
        img=Image.fromarray(image)
        img=img.resize((550,550))
        render_image(img)
        
#  funcation blur image
def apply_blur():
    if original_image is not None:
        blurred_image = cv2.GaussianBlur(original_image, (45, 45), 0)
        show_original(blurred_image)



        
# apply color funcation
def apply_color_change(color):
    if original_image is not None:
        r, g, b = color
        enhanced_image = original_image.copy()
        enhanced_image[:, :, 0] = np.clip(enhanced_image[:, :, 0] * (b / 255), 0, 255).astype(np.uint8)
        enhanced_image[:, :, 1] = np.clip(enhanced_image[:, :, 1] * (g / 255), 0, 255).astype(np.uint8)
        enhanced_image[:, :, 2] = np.clip(enhanced_image[:, :, 2] * (r / 255), 0, 255).astype(np.uint8)
        show_original(enhanced_image)

#rotate image funcation
def rotate_image(angle=45):
    if original_image is not None:
        height, width = original_image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
        show_original(rotated_image)

#resize image funcation
def resize_image(width, height):
    if original_image is not None:
        resized_image = cv2.resize(original_image, (width, height), interpolation=cv2.INTER_LINEAR)
        show_original(resized_image)

#sharpen image funcation
def apply_sharpen():
    if original_image is not None:
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
        sharpened_image = cv2.filter2D(original_image, -1, kernel)
        show_original(sharpened_image)


def render_image(image):
    photo = ImageTk.PhotoImage(image=image)
    canvas.image = photo
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

#resize image funcation
def get_resize_dimensions():
    width = int(width_entry.get())
    height = int(height_entry.get())
    resize_image(width, height)

#choose color funcation
def choose_color():
    color = colorchooser.askcolor()[0]
    if color:
        apply_color_change(color) 

# save funcation
def save_image():
    global original_image
    if original_image is not None:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if filename:
            # Convert OpenCV image (BGR) to PIL Image (RGB)
            pil_image = Image.fromarray(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
            # Save the PIL Image
            pil_image.save(filename)
            print("Image saved successfully:", filename)
        else:
            print("Save operation canceled.")
    else:
        print("No image to save.")

#main window
main=tk.Tk()
main.title('IMAGE EDITING')
main.maxsize(1530,780)
main.minsize(1530,780)


# title lable
title_lable=tk.Label(text='IMAGE EDITOR',font=('arial',50,'bold'),relief=tk.GROOVE,bg='gray',bd=12)
title_lable.pack(fill='x')

#body lable
body_lable=tk.Label(relief=tk.GROOVE,bg='gray',bd=12,height=45)
body_lable.pack(fill='x')


#left frame
left_frame=tk.Label(body_lable,relief=tk.GROOVE,bg='skyblue',bd=7,width=110,height=39)
left_frame.place(x=30,y=30)


#right frame
right_frame=tk.Label(body_lable,relief=tk.GROOVE,bg='skyblue',bd=7,width=84,height=39)
right_frame.place(x=860,y=30)



# path entry
path_lable=tk.Label(left_frame,text='CHOOSE IMAGE',font=('arial',15,'bold'),bg='lightblue',bd=4)
path_lable.place(x=30,y=40)
path_entry=tk.Entry(left_frame,width=40,bd=5,font=('arial',10))
path_entry.place(x=250,y=40)

original_image=None
#browse button
browse_button=tk.Button(left_frame,text='Browse',bd=5,width=7,height=1,font=('arial',10,'bold'),activebackground='skyblue',command=load_image)
browse_button.place(x=620,y=40)

# show orginal button
show_button = tk.Button(left_frame, text='Show Orginal', bd=5, width=12, height=2, font=('arial', 10, 'bold'), activebackground='skyblue', command=lambda: show_original(original_image))
show_button.place(x=220, y=110)

# Blur Button
blur_button=show_button=tk.Button(left_frame,text='Blur',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=apply_blur)
blur_button.place(x=100,y=240)


#Sharpen button
sharpen_button=show_button=tk.Button(left_frame,text='Sharpen',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=apply_sharpen)
sharpen_button.place(x=330,y=240)





#rotate button
#rotate_45
rotate_45=show_button=tk.Button(left_frame,text='Rotate 45°',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=lambda:rotate_image(45))
rotate_45.place(x=100,y=340)

#rotate_90
rotate_90=show_button=tk.Button(left_frame,text='Rotate 90°',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=lambda:rotate_image(90))
rotate_90.place(x=330,y=340)

#rotate_180
rotate_180=show_button=tk.Button(left_frame,text='Rotate 180°',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=lambda:rotate_image(180))
rotate_180.place(x=550,y=340)


#color button
color_button=show_button=tk.Button(left_frame,text='Color',bd=5,width=12,height=2,font=('arial',10,'bold'),activebackground='skyblue',command=choose_color)
color_button.place(x=550,y=240)


#resize image
resize_label = tk.Label(left_frame, text="Resize (Width x Height):",bg='skyblue',font=('arial',13,'bold'))
resize_label.place(x=170,y=450)

width_entry = tk.Entry(left_frame,bd=5)
width_entry.place(x=380,y=440)
width_entry.insert(0, "550")

height_entry = tk.Entry(left_frame,bd=5)
height_entry.place(x=380,y=480)
height_entry.insert(0, "550")

resize_button = tk.Button(left_frame, text="Resize",bd=5,activebackground='lightblue',font=('arial',10,'bold'),command=get_resize_dimensions)
resize_button.place(x=550,y=460)

# Save Button
save_button = tk.Button(left_frame, text="Save", bd=5, width=12, height=2, font=("arial", 10, "bold"), activebackground="skyblue", command=save_image)
save_button.place(x=440, y=110)

canvas = tk.Canvas(right_frame, width=545, height=545,bg='skyblue')
canvas.place(x=20,y=20)

main.mainloop()