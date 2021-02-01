import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+400+150")


label = tkinter.Label(win, text="*********", bg="red")
# 设置焦点
label.focus_set()
label.pack()

def function(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)


win.bind("a", function) # 注意前面改成了win，只需要写出按键名即可


win.mainloop()