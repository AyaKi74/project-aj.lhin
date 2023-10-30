from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry("1440x810")

bg_image = Image.open("f_page_resize.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


button_image =Image.open(r"D:\wallpapers\profile .png") 
button_photo = ImageTk.PhotoImage(button_image)

# Create the button with the button image
button = Button(root, text="A", image=button_photo, borderwidth=0)
button.place(x=325, y=305)
# b2 = Button(root, text="B", borderwidth=0, width=120, height=3, highlightthickness=0)
# b2.place(x=325, y=430)

root.mainloop()



