from tkinter import *
import tkinter.filedialog
import base64
root= Tk() 
from tkinter.scrolledtext import ScrolledText
# 解码
def baseConvert(encoded_data):
	# encoded_data=b'dmVyc2lvbj0xJnRpbWVzdGFtcD0yMDE5MTAwMTA5MTIyMSZyZXF1ZXN0X2lkPTEyMzQ1NiZzb3VyY2Vfc3lzdGVtPWhpcyZvYmplY3Rfc3lzdGVtPWxpcyZhY3Rpb249cmVxdWVzdF9jYWxsJmNvZGU9bGlzNDE='
	scr.delete(1.0, END)
	decoded_data = base64.b64decode(encoded_data).decode('utf-8')
	scr.insert(END,decoded_data)
# 编码
def baseConvert2(encoded_data):
	# encoded_data=b'dmVyc2lvbj0xJnRpbWVzdGFtcD0yMDE5MTAwMTA5MTIyMSZyZXF1ZXN0X2lkPTEyMzQ1NiZzb3VyY2Vfc3lzdGVtPWhpcyZvYmplY3Rfc3lzdGVtPWxpcyZhY3Rpb249cmVxdWVzdF9jYWxsJmNvZGU9bGlzNDE='
	scr2.delete(1.0, END)
	decoded_data = base64.b64encode(encoded_data.encode('utf-8'))
	scr2.insert(END,decoded_data)

cavans=Canvas(root,height=800,width=1200,bg='#EEC900',bd=0)
cavans.pack()

frame=Frame(cavans,background="#C0FF3E")
frame.place(relx=0.05,rely=0,relwidth=0.9,relheight=1)

l1=Label(frame,text='输入需要解码内容',bg='#FF34B3')
l1.place(relx=0,rely=0.1,relwidth=0.15,relheight=0.1)
l2=Label(frame,text='输入需要编码内容',bg='#FF34B3')
l2.place(relx=0.52,rely=0.1,relwidth=0.15,relheight=0.1)
dp=Entry(frame,text ='解码内容',bg='#54FF9F')
dp.place(relx=0,rely=0.2,relwidth=0.45,relheight=0.2)
dp2=Entry(frame,text ='编码内容',bg='#54FF9F')
dp2.place(relx=0.52,rely=0.2,relwidth=0.45,relheight=0.2)

btnsm = Button(frame,text="解密",bg='red',command=lambda:baseConvert(dp.get()),fg="yellow")
btnsm.place(relx=0.37,rely=0.1,relwidth=0.08,relheight=0.1)

btnjm = Button(frame,text="加密",bg='red',command=lambda:baseConvert2(dp2.get()),fg="yellow")
btnjm.place(relx=0.89,rely=0.1,relwidth=0.08,relheight=0.1)
scr =ScrolledText(frame,bg='#7FFF00') 
scr.place(relx=0,rely=0.4,relwidth=0.45,relheight=1)
scr2 =ScrolledText(frame,bg='#7FFF00') 
scr2.place(relx=0.52,rely=0.4,relwidth=0.45,relheight=1)

root.mainloop() 

# from tkinter import *
# import tkinter.filedialog
# import base64

# class Window:
# 	def __init__(self,handle):
# 		self.win = handle
# 		self.createwindow()
# 		self.run()
		
# 	def createwindow(self):
# 		self.win.geometry('400x400')
# 		#label 1
# 		self.label_text = StringVar()
# 		self.label_text.set("----")
# 		self.lable = Label(self.win,
# 					textvariable=self.label_text,
# 					font=('Arial',11),width=15,height=2)
# 		self.lable.pack()

# 		#text_contrl
# 		self.entry_text = StringVar()
# 		self.entry = Entry(self.win,textvariable=self.entry_text,width=30)
# 		self.entry.pack()

# 		#button
# 		self.button =Button(self.win,text="set label to text",width=15,height=2,command=self.setlabel)
# 		self.button.pack()

# 	def setlabel(self):
# 		print(self.entry_text.get())
# 		self.label_text.set(self.entry_text.get())

# 	def run(self):
# 		try:
# 			self.win.mainloop()
# 		except Exception as e:
# 			print ("*** exception:\n".format(e))

# window= Tk() 
# window.title('hello tkinter')
# Window(window).run()
# window.mainloop()
