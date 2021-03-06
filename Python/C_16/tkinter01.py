import tkinter as Tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Tk.Frame(self, master)
        self.button1 = Tk.Button(
            self.frame, text="New Window", width=25, command=self.new_window
        )
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = Tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Tk.Frame(self, master)
        self.quitButton = Tk.Button(
            self.frame, text="Quit", width=25, command=self.close_windows
        )
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
