from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#创建两个按钮
b1=Button(myWindow, text='button1',bg="red", relief='raised', width=8, height=2)
b1.grid(row=0, column=0, sticky=W, padx=5,pady=5)
b2=Button(myWindow, text='button2', font=('Helvetica 10 bold'),width=8, height=2)
b2.grid(row=0, column=1, sticky=W, padx=5, pady=5)
#进入消息循环