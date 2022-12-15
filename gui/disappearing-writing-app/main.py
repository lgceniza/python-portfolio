from tkinter import Tk, Frame, Text, Scrollbar, BOTH, RIGHT, LEFT, VERTICAL

# TODO: start timer whenever user stops keypress
# TODO: stop timer whenever user starts keypress
# TODO: clear editor text whenever timer runs out

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.font = ("Georgia", 20, "normal")
    self.init_window()

  def init_window(self):
    self.master.title("Disappearing Writing App")
    self.pack(fill=BOTH, expand=1)

    self.scrollbar = Scrollbar(self, orient=VERTICAL)
    self.scrollbar.pack(side=RIGHT, fill='y')
    self.editor = Text(self, font=self.font, padx=50, pady=30, highlightthickness=0, spacing3=5, yscrollcommand=self.scrollbar.set)
    self.scrollbar.config(command=self.editor.yview)
    self.editor.pack(fill=BOTH, expand=1, side=LEFT)
    self.editor.focus()


screen = Tk()
screen.geometry('800x600')

window = Window(screen)
window.mainloop()
