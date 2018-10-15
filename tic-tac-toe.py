from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player
      button["bg"] = "yellow"

      if player == "X" :
            player = "A"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
sdsdsds
window = Tk()
player = "X"
list= []

for i in range(12) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//4, column=i%4)
      list.append(b)

window.mainloop()
