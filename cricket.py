import tkinter as tk
from PIL import ImageTk, Image
import os
from bs4 import BeautifulSoup
import urllib.request
score_page = 'http://static.cricinfo.com/rss/livescores.xml'    
page = urllib.request.urlopen(score_page)
soup = BeautifulSoup(page, 'html.parser')
result = soup.find_all('description') 

ls=[]
for match in result:
    ls.append(match.get_text())

def score():
    T.insert(tk.END,ls)
def clear():
    T.delete(1.0,tk.END)
root = tk.Toplevel()
root.geometry('900x700')
pilImage = Image.open("sample.jpeg")
img = ImageTk.PhotoImage(pilImage)
panel = tk.Label(root, image = img)
panel.place(x=0,y=0)
T=tk.Text(root)
T.place(x=310,y=100,height=200,width=400)
l=tk.Label(root,text="LIVE SCORE \n ©Copyright @Zyed",fg="white",bg="black")
l.place(x=420,y=50,height=50,width=150)
b1=tk.Button(root,text="Score",bg="black",fg="red",command=score)
b1.place(x=310,y=300,height=75,width=150)
b2=tk.Button(root,text="Clear",bg="black",fg="red",command=clear)
b2.place(x=560,y=300,height=75,width=150)
root.mainloop()
