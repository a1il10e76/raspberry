#coding:utf-8
import tkinter
from tkinter import *
from tkinter import ttk
def btn_click(event):
    if event.widget['bg'] == '#FF0000':
        event.widget['bg'] = '#FFFFFF'
    else:
        event.widget['bg'] = '#FF0000'
        hancho_box[0].current(0)

root = Tk()
root.geometry('500x500')
root.title('出勤表')

#リスト定義
kacho = []
kakaricho = []
hancho = []
hancho_box = []
member = []
member_box = []
kacho_number = [2505]
kakaricho_number = [2501,2502]
number = ['----','昼勤',2508,2509,2522,'遅番',2524,2523,2524,'夜勤',2507,2503,2525]
late_number = []
night_number = []
#名前入力
kacho_list = ['佐藤']
kakaricho_list = ['木原','樫本']
hancho_list = ['石中','田中','亀田','藤内']                                                                             
member_list = ['中谷','藤原','宗野','齋藤','石川','永嶋','西田','大坪','茂野','塩滿','河野','竹内','谷野']
kacho_num = len(kacho_list)
kakaricho_num = len(kakaricho_list)
hancho_num = len(hancho_list)
member_num = len(member_list)
#ボタン定義
for i in range(kacho_num):
    kacho.append(tkinter.Button(root,text = kacho_list[i] + '課長',bg = '#FF0000',width = 4))
for i in range(kakaricho_num):
    kakaricho.append(tkinter.Button(root,text = kakaricho_list[i] + '係長',bg = '#FF0000',width = 4))
for i in range(hancho_num):
    hancho.append(tkinter.Button(root,text = hancho_list[i] + '班長',bg = '#FF0000',width = 4))
    hancho_box.append(ttk.Combobox(root,state='readonly',width = 5,values=(number)))
for i in range(member_num):
    member.append(tkinter.Button(root,text = member_list[i],bg = '#FF0000',width = 4))
    member_box.append(ttk.Combobox(root,state='readonly',width = 5,values=(number)))
#ボタン配置
kacho[0].grid(row = 8,column = 0)
kakaricho[0].grid(row = 4,column = 1)
kakaricho[1].grid(row = 12,column = 1)
hancho[0].grid(row = 1,column = 3); hancho_box[0].grid(row = 1,column = 4)
hancho[1].grid(row = 3,column = 3)
hancho[2].grid(row = 6,column = 3)
hancho[3].grid(row = 14,column = 3)
member[0].grid(row = 2,column = 4)
member[1].grid(row = 4,column = 4)
member[2].grid(row = 5,column = 4)
member[3].grid(row = 7,column = 4)
member[4].grid(row = 10,column = 3)
member[5].grid(row = 9,column = 4)
member[6].grid(row = 10,column = 4)
member[7].grid(row = 11,column = 4)
member[8].grid(row = 12,column = 4)
member[9].grid(row = 13,column = 4)
member[10].grid(row = 15,column = 4)
member[11].grid(row = 16,column = 4)
member[12].grid(row = 1,column = 5)
#ボタンクリック処理
for i in range(kacho_num):
    kacho[i].bind('<1>',btn_click)
for i in range(kakaricho_num):
    kakaricho[i].bind('<1>',btn_click)
for i in range(hancho_num):
    hancho[i].bind('<1>',btn_click)
for i in range(member_num):
    member[i].bind('<1>',btn_click)
root.mainloop()
