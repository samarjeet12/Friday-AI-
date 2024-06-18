import os
try:
    import tkinter as tk
except:
    os.system("pip install tk")
    import tkinter as tk

try: 
    from PIL import Image, ImageTk
except:
    os.system("pip install pillow")
    from PIL import Image, ImageTk

class GIFPlayerApp:
    def __init__(self, master, gif_path):
        self.master = master
        self.gif_path = gif_path

        self.gif = Image.open(gif_path)
        self.gif_frames = []
        self.current_frame_index = 0

        self.load_frames()

        self.label = tk.Label(master)
        self.label.pack()

        self.play()


    def load_frames(self):
        try:
            while True:
                self.gif.seek(len(self.gif_frames))
                frame = self.gif.copy()
                self.gif_frames.append(ImageTk.PhotoImage(frame))
        except EOFError:
            pass

    def play(self):
        self.show_frame()

    def show_frame(self):
        self.label.config(image=self.gif_frames[self.current_frame_index])
        self.current_frame_index += 1
        if self.current_frame_index >= len(self.gif_frames):
            self.current_frame_index = 0
        self.master.after(20, self.show_frame)

        

def main():
    root = tk.Tk()
    root.title("F.R.I.D.A.Y")
    gif_path = "friday_gui.gif"  
    app = GIFPlayerApp(root, gif_path)
    root.mainloop()

if __name__ == "__main__":
    main()
