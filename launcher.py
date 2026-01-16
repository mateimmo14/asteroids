import official_main
import tkinter as tk
import time



def main():
    root = tk.Tk()
    def launch_easy():
        root.destroy()
        official_main.main(False)
    def run_easy():
        launch_button.configure(text="Launching...")

        root.after(1000, launch_easy)
    def launch_hard():
        root.destroy()
        official_main.main(True)
    def run_hard():
        hard_launch_button.configure(text="Launching...")
        root.after(1000, launch_hard)


    root.title("Asteroids launcher")
    root.geometry("700x600")

    launch_button = tk.Button(root, text="Press to launch normal mode", bg="green",fg="white",font=("Sans Serif", 20, "bold"), command=run_easy)
    launch_button.pack(pady=80,ipady=100, ipadx=50)
    hard_launch_button = tk.Button(root, text="Press to launch hard mode", bg="red",fg="white",font=("Sans Serif", 15, "bold"), command=run_hard)
    hard_launch_button.pack(pady=10,ipady=25, ipadx=17.5)
    root.mainloop()
main()
