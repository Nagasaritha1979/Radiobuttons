from tkinter import *
from PIL import Image,ImageTk


def sel():
   selection = "You selected " + str(var.get())
   label.config(text = selection)

root = Tk()
var = StringVar(value=' ')


image=Image.open('visa.jpg')         # i have placed the image in default directory and given just the file name visa.jpg
image1=Image.open('master card.png')
image2=Image.open('American express.png')
image3=Image.open('paypal.jpg')

img=image.resize((50,50))
img1=image1.resize((50,50))
img2=image2.resize((50,50))
img3=image3.resize((50,50))


my_img=ImageTk.PhotoImage(img,master=root)
my_img1=ImageTk.PhotoImage(img1,master=root)
my_img2=ImageTk.PhotoImage(img2,master=root)
my_img3=ImageTk.PhotoImage(img3,master=root)

L1=Label(root,text='Payment Method',font=("Arial",25),fg='blue')
L1.pack(side=TOP)


R1 = Radiobutton(root, text="Visa", image=my_img,compound='left',variable=var,value='Visa',
                  command=sel,font=("Arial",25),padx=50,pady=50)

R1.pack(anchor = W)

R2 = Radiobutton(root, text="Master Card",variable=var,image=my_img1,compound='left',value='Master Card',
                  command=sel,font=("Arial",25),padx=50,pady=50)
#R2.image=my_img1
R2.pack(anchor = W)

R3 = Radiobutton(root, text="American Express", image=my_img2,compound='left',variable=var,value='American Express',
                  command=sel,font=("Arial",25),padx=50,pady=50)
#R3.image=my_img2
R3.pack(anchor = W)

R4 = Radiobutton(root, text="PayPal", image=my_img3,compound='left',variable=var,value='PayPal',
                  command=sel,font=("Arial",25),padx=50,pady=20)

#R4.image=my_img3
R4.pack(anchor = W)

label = Label(root,font=("Arial",15))
label.pack()
root.mainloop()
