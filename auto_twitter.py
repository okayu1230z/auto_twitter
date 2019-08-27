import os
import sys
import tkinter as Tk
import twitter
import requests
import datetime
from bs4 import BeautifulSoup
# from dotenv import find_dotenv, load_dotenv

api = twitter.Api(consumer_key="WbMVdi4evgEwo5MefQcxou0JZ",
                  consumer_secret="uWDfxLwKJbG1h62XmOL0Fohxv0cAHk6r2wst3l8knX0gViRNSW",
                  access_token_key="1131453470588882945-I1QKaVtlJlzmcRn94Gqf9icgFO2IO7",
                  access_token_secret="gkF8viz8QWXletzlWhWr7eb4K3Zw2HjEmdE2Bv2YoRauD")

#t = twitter.Twitter(auth=auth)

url = 'https://tenki.jp/forecast/3/16/4410/13208/'
r = requests.get(url)

class Frame(Tk.Frame):
     def __init__(self, master=None):
         Tk.Frame.__init__(self, master)
         self.master.title("おーとついったー")

#         bt_nini = Tk.Button(self, text="任意文字ツイート", bg='#c0c0c0', fg='#000000', font=("", 20), command=pushed_nini)
#         bt_nini.pack(padx=5, pady=5, fill=Tk.X)
         
         bt_gm1 = Tk.Button(self, text="起床", bg='#c0c0c0', fg='#000000', font=("", 20), command=pushed_gm1)
         bt_gm1.pack(padx=5, pady=5, fill=Tk.X)

         bt_gm2 = Tk.Button(self, text="絶望の起床" , bg='#c0c0c0', fg='#000000', font=("", 20), command=pushed_gm2)
         bt_gm2.pack(padx=5, pady=5, fill=Tk.X)

         bt_tenki = Tk.Button(self, text="天気" , bg='#c0c0c0', fg='#000000', font=("", 20), command=pushed_tenki)
         bt_tenki.pack(padx=5, pady=5, fill=Tk.X)

         bt_ga = Tk.Button(self, text="寝る" ,bg='#c0c0c0', fg='#000000', font=("", 20), command=pushed_ga)
         bt_ga.pack(padx=5, pady=5, fill=Tk.X)

         bt_ex = Tk.Button(self, text="閉じる", bg='#c0c0c0', fg='#000000', font=("", 20), command=sys.exit)
         bt_ex.pack(padx=5, pady=5, fill=Tk.X)

def pushed_gm1():
    api.PostUpdate("ぽきた")

def pushed_gm2():
    api.PostUpdate("絶起した")

def pushed_tenki():
    bsObj = BeautifulSoup(r.content, "html.parser")

    today = bsObj.find(class_="today-weather")
    weather = today.p.string

    temp=today.div.find(class_="date-value-wrap")

    temp=temp.find_all("dd")
    temp_max = temp[0].span.string 
    temp_max_diff=temp[1].string 
    temp_min = temp[2].span.string 
    temp_min_diff=temp[3].string 

    dt = datetime.datetime.today()
    
    api.PostUpdate(str(dt.year) + "年" + str(dt.month) + "月" + str(dt.day) + "日" + " 本日の天気:{}".format(weather) + "\n 最高気温:{} {}".format(temp_max,temp_max_diff) + "\n 最低気温:{} {}".format(temp_min,temp_min_diff))

def pushed_ga():
    api.PostUpdate("寝ます")

def pushed_ex():
    print("clicked")
 
    
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
