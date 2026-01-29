import tkinter as tk
from PIL import Image, ImageTk
import os
import numpy as np
import random

class application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Guessing LOL Skill')
        self.geometry('723x900+600+100')
        self.configure(bg='#5f6160')

        current_path = os.getcwd()

        self.path = os.path.join(current_path, 'Champion_Gallery')
        champion_allname = open(os.path.join(current_path, "Champion_Names/champNames.txt"), "r")
        champion_name_list = champion_allname.read()
        champion_name_list = champion_name_list.split('\n')
        self.show_champion_listbox = champion_name_list.copy()
        champion_allname.close()
        self.champion_gallery = os.listdir(self.path)
        champion = str(random.choice(self.champion_gallery))
        self.champion_Name = champion[:-5].upper()
        self.champion_Skill = champion[-5].upper()
        self.score = 0
        
        self.champion_picture = Image.open(self.path + '/' + champion)
        self.resized_champion_picture = self.champion_picture.resize((200, 200), Image.ANTIALIAS)
        self.new_champion_picture = ImageTk.PhotoImage(self.resized_champion_picture)

        self.champion_picture_show = tk.Label(self, image=self.new_champion_picture, width=200, height=200, borderwidth=10, bg='white')
        self.entrybox = tk.Entry(self, width=10, font="Thaisarabun 30")
        self.entrybox_skill = tk.Entry(self, width=10, font="Thaisarabun 30")
        self.listbox = tk.Listbox(self, width=10, height=5, font="Thaisarabun 30")
        self.listbox_skill = tk.Listbox(self, width=10, height=5, font="Thaisarabun 30")
        self.confirmButton = tk.Button(self, text='CONFIRM', font="Thaisarabun 30", command=self.checkAnswer)

        self.label_skill = tk.Label(self, text='SKILL', font="Thaisarabun 30")
        self.label_score = tk.Label(self, text=f'Score: {self.score}', font="Thaisarabun 30")
        self.label_wrong = tk.Label(self, text="Wrong", font="Thaisarabun 30")

        self.blank = tk.Label(self, font="Angsananew 80", bg='#5f6160')
        self.blank2 = tk.Label(self, font="Angsananew 30", bg='#5f6160')
        self.blank3 = tk.Label(self, font="Angsananew 10", bg='#5f6160')

        # init listbox
        for champ in champion_name_list:
            self.listbox.insert(tk.END, champ)

        self.label_score.pack(pady=20)
        self.champion_picture_show.pack()
        self.blank2.pack()
        self.entrybox_skill.pack()
        self.entrybox.pack()
        self.listbox.pack()
        self.blank3
        self.confirmButton.pack(pady=20)
        
        self.entrybox_skill.focus()

        self.entrybox_skill.bind('<Return>', lambda *args: self.entrybox.focus())
        self.entrybox.bind('<KeyRelease>', self.scanKey)
        self.entrybox.bind('<Return>', self.checkAnswer)
        self.listbox.bind('<<ListboxSelect>>', self.selectListBox)

    def scanKey(self, event):
        templist = []
        self.listbox.delete(0, tk.END)
        text = self.entrybox.get()
        text = text.upper()
        for champ in self.show_champion_listbox:
            if text in champ:
                templist.append(champ)
        for champ in templist:
            self.listbox.insert(tk.END, champ)

    def selectListBox(self, event: tk.Event):
        widget: tk.Listbox = event.widget
        index = widget.curselection()[0]
        value = widget.get(index)
        self.entrybox.delete(0, tk.END)
        self.entrybox.insert(0, value)

    def nextStage(self):
        champion = str(random.choice(self.champion_gallery))
        self.champion_Name = champion[:-5].upper()
        self.champion_Skill = champion[-5].upper()
        self.champion_picture = Image.open(self.path + '/' + champion)
        self.resized_champion_picture = self.champion_picture.resize((200, 200), Image.ANTIALIAS)
        self.new_champion_picture = ImageTk.PhotoImage(self.resized_champion_picture)
        self.champion_picture_show.configure(image=self.new_champion_picture)

        self.listbox.delete(0, tk.END)
        for champ in self.show_champion_listbox:
            self.listbox.insert(tk.END, champ)

        self.entrybox_skill.delete(0, tk.END)
        self.entrybox.delete(0, tk.END)
        self.entrybox_skill.focus()
        
        self.label_wrong.destroy()
        self.label_wrong = tk.Label(self, text="Wrong", font="Thaisarabun 30")

    
    def checkAnswer(self, *args):
        input_skill = self.entrybox_skill.get()
        input_champion = self.entrybox.get()
        print(input_skill, input_champion)
        print(self.champion_Skill, self.champion_Name)
        if input_skill.upper() == self.champion_Skill and input_champion.upper() == self.champion_Name:
            self.nextStage()
            self.score += 1
            self.label_score.configure(text=f'Score: {self.score}')
        else:
            self.label_wrong.pack()
            self.entrybox_skill.delete(0, tk.END)
            self.entrybox.delete(0, tk.END)
            self.entrybox_skill.focus()
            self.listbox.delete(0, tk.END)
            for champ in self.show_champion_listbox:
                self.listbox.insert(tk.END, champ)

if __name__ == "__main__":
    game = application()
    game.mainloop()