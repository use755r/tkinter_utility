from tkinter import *
from tkinter import filedialog as fd
import os
root = Tk()

class MainWindow:
	def __init__(self, master):
		self.master = master
		self.f_top = Frame(self.master)
		self.f_bot = Frame(self.master)
		
		#параметры окна
		self.master.title('List Folder')
		self.master.geometry='420x400'
		self.master.config(bg='#4F5A6E')
		
		#описание элементов
		self.text = Text(self.f_bot,width=50, bg='#EEF1F4')
		self.button_select_folder = Button(self.f_top,text='Select Folder', bg='#616D84', fg='#EEF1F4')
		self.button_save = Button(self.f_top, text='Save result', bg='#616D84', fg='#EEF1F4')
		self.scroll = Scrollbar(self.f_bot,command=self.text.yview)
		self.text.config(yscrollcommand=self.scroll.set)
		
		#вставка элементов
		self.f_top.pack()
		self.f_bot.pack()
		self.button_select_folder.pack(side=LEFT)
		self.button_save.pack(side=RIGHT)
		self.text.pack(side=LEFT)
		self.scroll.pack(side=RIGHT, fill=Y)

		#вызов событий
		self.button_select_folder['command']=lambda:self.open_folder()
		self.button_save['command']=lambda:self.save_file()
	
	def open_folder(self):
		path_folder = fd.askdirectory()
		lst_folder = os.listdir(path_folder)
		self.text.delete(1.0, END)
		for i in lst_folder:
			self.text.insert(1.0, str(i+'\n'))
	
	def save_file(self):
		file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
		f = open(file_name, 'w')
		s = self.text.get(1.0, END)
		f.write(s)
		f.close()
			
		
		 
		
	
main_window = MainWindow(root)

if __name__=='__main__':
	root.mainloop()
		
