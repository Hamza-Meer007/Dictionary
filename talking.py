from tkinter import *
import json
from tkinter import messagebox
from difflib import get_close_matches
import pyttsx3
import os

# Construct an absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct an absolute path to the files
data_json_path = os.path.join(script_dir, "assets", "data.json")
dic_ico_path = os.path.join(script_dir, "assets", "dic.ico")
bg_png_path = os.path.join(script_dir, "assets", "bg.png")
search_png_path = os.path.join(script_dir, "assets", "search.png")
mic_png_path = os.path.join(script_dir, "assets", "mic.png")
microphone_png_path = os.path.join(script_dir, "assets", "microphone.png")
exit_png_path = os.path.join(script_dir, "assets", "exit.png")
clear_png_path = os.path.join(script_dir, "assets", "clear.png")


def search_data():
    data= json.load(open(data_json_path))
    word1 = word_entry.get().lower()
    
    if word1 in data:
        meaning = data[word1]
        text_area.delete(1.0,END)
        for item in meaning:
            text_area.insert(END,f"\u2022 {item} \n\n")
    elif len(get_close_matches(word1,data))>0:
        close=get_close_matches(word1,data)[0]
        res = messagebox.askyesno("Confirm",f"Do you mean '{close}' instead?")
        if res:
            word_entry.delete(0,END)
            word_entry.insert(0,close)
            text_area.delete(1.0,END)
            meaning = data[close]
            for item in meaning:
                text_area.insert(END,f"\u2022 {item} \n\n")
        else:
            messagebox.showerror("Error","Kindly re-check it.The word doesn't exist")
    else:
        messagebox.showinfo("Information","The word doesn't exist")
        text_area.delete(1.0,END)
        word_entry.delete(0,END)




engine = pyttsx3.init()

voice = engine.getProperty("voices")
engine.setProperty("voices",voice[1].id)

def iexit():
    res=messagebox.askyesno("Confirm","Do you want to exit?")
    if res:
        root.destroy()
    else:
        pass

def clear_all():
    word_entry.delete(0,END)
    text_area.delete(1.0,END)


def read():
   
    engine.say( word_entry.get())
    engine.runAndWait()


def read_meaning():
    engine.say(text_area.get(1.0,END))
    engine.runAndWait()




root= Tk()
root.title("Talking Dictionary created by Hamza Meer")

root.geometry("1000x626+150+40")
root.resizable(0,0)

root.iconbitmap(dic_ico_path)

bg= PhotoImage(file=bg_png_path)
bg_label= Label(root,image=bg)
bg_label.place(relwidth=1,relheight=1)

word = Label(root,text="Enter a Word ",font="Times 25 bold underline ",bg="whitesmoke",fg="red3")
word.place(x=650,y=40)

word_entry=Entry(root,font="Times 23 bold",bd=8,relief="groove",justify=CENTER)
word_entry.place(x=600,y=100)

search_img= PhotoImage(file=search_png_path)

search= Button(root,image=search_img,bd=0,activebackground="whitesmoke",cursor="hand2",command=search_data)
search.place(x=670,y=160)

mic_img= PhotoImage(file=mic_png_path)

mic= Button(root,image=mic_img,bd=0,activebackground="whitesmoke",bg="whitesmoke",cursor="hand2",command=read)
mic.place(x=790,y=160)


meaning = Label(root,text="Meaning ",font="Times 28 bold underline ",bg="whitesmoke",fg="red3")
meaning.place(x=690,y=250)

text_area= Text(root,width=38,height=9,bd=8,relief="groove",font="arial 14 bold",wrap=WORD)
text_area.place(x=550,y=310)


microphone_img= PhotoImage(file=microphone_png_path)

microphone= Button(root,image=microphone_img,bd=0,activebackground="whitesmoke",bg="whitesmoke",cursor="hand2",command=read_meaning)
microphone.place(x=730,y=540)


exit_img= PhotoImage(file=exit_png_path)

exit= Button(root,image=exit_img,bd=0,activebackground="whitesmoke",bg="whitesmoke",cursor="hand2",command=iexit)
exit.place(x=840,y=540)

clear_img= PhotoImage(file=clear_png_path)

clear= Button(root,image=clear_img,bd=0,activebackground="whitesmoke",bg="whitesmoke",cursor="hand2",command=clear_all)
clear.place(x=620,y=540)

def enter(event):
    search.invoke()

def saaf(eve):
    exit.invoke()

root.bind("<Return>",enter)
root.bind("<Escape>",saaf)

root.mainloop()