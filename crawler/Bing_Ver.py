import os
import tkinter
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import getpass 
from icrawler.builtin import BingImageCrawler

# Get User name 
username = getpass.getuser() 
idir = "C:\\Users\\" + username + "\\Downloads"

# select file
def file_select():
  file_path = tkinter.filedialog.askdirectory(initialdir = idir)
  folder_path.delete(0,"end")
  folder_path.insert(tkinter.END, file_path)

# String validation
def validation(before_word, after_word):
    return ((after_word.isdecimal()) and (len(after_word)<=4)) or (len(after_word) == 0)

def pring():
  # new folder name
  new_path = folder_path.get() + "\\" + folder_name.get()
  if not os.path.exists(new_path):
    # make new folder
    os.mkdir(new_path)
    # print("create new folder")
    # main program
    crawler = BingImageCrawler(storage={"root_dir":new_path})
    if combo_1.get() != "None":
      filters = dict(size=combo_1.get())
    else :
      filters = None
    crawler.crawl(keyword=picture_name.get(),filters=filters,offset=0, max_num=int(picture_num.get()))
    res = messagebox.askokcancel('finished!!!', 'Reset input, but check folder?')
    folder_name.delete(0,"end")
    picture_name.delete(0,"end")
    picture_num.delete(0,"end")
    if res :
      tkinter.filedialog.askopenfilename(initialdir = new_path)
  else :
    
    messagebox.showinfo('failed...', 'A folder with the same name already exists\n' + new_path)

# String validation
def validation(before_word, after_word):
    return ((after_word.isdecimal()) and (len(after_word)<=4)) or (len(after_word) == 0)


# make window
root = tkinter.Tk()
root.title("images collection_Bing")
root.geometry("340x360")

button = tkinter.Button(text="Change",command=file_select,height = 1, width = 7,)
button.place(x=275, y=24)

#file Choice
folder_path = tkinter.Entry(font=("10","10"),width=37)
folder_path.insert(0, "C:\\Users\\" + username + "\\Downloads")
folder_path.place(x=10, y=30)

folder_name = tkinter.Entry(font=("15","25"),width=19)
folder_name.place(x=10, y=80)

# font
font1 = font.Font(size=15,weight='bold')

# other
label_1 = tkinter.Label(text="Directory to create folder", font=font1)
label_1.place(x=7, y=0)

label_2 = tkinter.Label(text="NEW folder name", font=font1)
label_2.place(x=7, y=50)

button_1 = tkinter.Button(text="Start collecting",command=pring,height = 2, width = 13,font=font1)
button_1.place(x=170, y=290)

button_2 = tkinter.Button(text="Finish",command=exit,height = 2, width = 12,font=font1)
button_2.place(x=7, y=290)

label_3 = tkinter.Label(text="What kind of images?", font=font1)
label_3.place(x=7, y=120)

picture_name = tkinter.Entry(font=("15","25"),width=19)
picture_name.place(x=10, y=150)

label_4 = tkinter.Label(text="How much?\n1~1000", font=font1)
label_4.place(x=35, y=190)

# entry
sv = tk.StringVar()
picture_num = tk.Entry(font=("15","25"),textvariable=sv,width=8)
vcmd = (picture_num.register(validation), '%s', '%P')
picture_num.configure(validate='key', vcmd=vcmd)
picture_num.place(x=195,y=200)

# saiz change
combo_1 = ttk.Combobox(root, state='readonly',height = 5, width = 10,font=font1) 
combo_1["values"] = ("None","small","medium","large")
combo_1.current(0)
combo_1.place(x=195,y=250)

label_5 = tkinter.Label(text="Image size", font=font1)
label_5.place(x=35, y=250)

# Not size change
root.resizable(0,0)

# mainloop
root.mainloop()