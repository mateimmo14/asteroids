import official_main
import tkinter as tk
import time



def main():
    root = tk.Tk()
    def launch():
        root.destroy()
        official_main.main()
    def run():
        launch_button.configure(text="Launching...")

        root.after(1000, launch)


    root.title("Asteroids launcher")
    root.geometry("600x500")

    launch_button = tk.Button(root, text="Press to launch", bg="red",fg="black",font=("Times New Roman", 30, "bold"), command=run)
    launch_button.pack(pady=80,ipady=100, ipadx=50)
    root.mainloop()
main()
