import os
import shutil
import tkinter as tk
from tkinter import messagebox

folders = ["files to sort","Images", "Videos", "Word files" , "Music" ,  
           "Other files" , "Apps","pdf files","powerpoint files","excel files"] 
for folder in folders :
    if   not os.path.exists(folder) :
       os.mkdir(folder) 
       
       
main_file = os.chdir("files to sort") 
files =  os.listdir(main_file)

excel = [".xlsx",".xls"]
pp = [".pptx"]
pdf = [".pdf"]
images= [".jpeg",".png",".jpg",".gif"] 
Word_files= [".doc",".txt",".docx",".rtf"] 
videos= [".mp4",".mkv" ,".mov"] 
music= [".mp3",".wav",".m4a"] 
applications= [".exe",".lnk"]
others = [""]


def all():
    
    for file in files:
            
        file_exe  = os.path.splitext(file)[1]
        
        if  file_exe in images:
            dest = "../Images"
            shutil.move(file,dest) 
                
        if file_exe in Word_files:
            dest = "../Word files"
            shutil.move(file,dest)   
            
        if file_exe in videos:
            dest ="../Videos"
            shutil.move(file,dest)
                
        if file_exe in applications:
            dest ="../Apps"
            shutil.move(file,dest)  
        
        if file_exe in music:
            dest ="../Music"    
            shutil.move(file,dest)
                
        if file_exe in pdf:
            dest="../pdf files"
            shutil.move(file,dest)
                
        if file_exe in pp:
            dest = "../powerpoint files" 
            shutil.move(file,dest) 
                
        if file_exe in excel:
            dest = "../excel files"
            shutil.move(file,dest)
               
        if file_exe in others:
            dest = "../Other files"
            shutil.move(file,dest)
                
    def massegebox(): 
                  
        massegebox  = messagebox.askyesno("File sorter" , """your files are now sorted 
         Do you want to exit ?""")
        
        
        if massegebox == True:
            root.destroy()
               
    massegebox()            
    
    
root =  tk.Tk()


root.title("File sorter")
root.geometry("500x300") 
frame =tk.Frame(root)
frame.grid(row=0 ,column=0 ) 

title = tk.Label(frame , text="Welcome to file sorter" ,font=("Arial" , 24))   
title.grid(row=0 , column=0 ,columnspan=3 ,pady=20 , padx=100)

text = tk.Label(frame , text="Please follow the following instructions:", font=("Arial" , 16))
text.grid(row=1 , column=0 )

first_instrc =tk.Label(root , text="1- Put the files you want to orgnize  in 'files to sort' folder" , font=('Arial' , 12 ))
first_instrc.place(x=15 , y=110)

secound_instrc =tk.Label(root, text="2- Click on 'sort files'" , font=('Arial' , 12 ))
secound_instrc.place(x=15 , y=135)

third_instrc =tk.Label(root , text="3- Your files will be orgnized automatically" , font=('Arial' , 12 ))
third_instrc.place(x=15 , y=160)
           
button =tk.Button(root , text="sort files"  , font=("Arial" , 14) ,command=all  ) 
button.place(x=210 , y= 200 )

root.mainloop()
                 