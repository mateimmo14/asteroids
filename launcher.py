import official_main
import tkinter as tk
import constants
import pygame
import sys
import os
from high_score import get_high_score_path
import os
def main():


    high_score_path = get_high_score_path()
    if not os.path.exists(high_score_path):
        # Create the file with default high score
        with open(high_score_path, "w") as f:
            f.write("0")

    # Now safely read the high score
    with open(high_score_path, "r") as f:
        content = f.read().strip()
        if content == "":
            high_score = 0
        else:
            high_score = int(content)

    # -----------------------------
    # INITIALIZE TKINTER WINDOW
    # -----------------------------
    root = tk.Tk()
    root.title("Asteroids Menu")
    root.geometry("1280x720")

    # -----------------------------
    # STORE SELECTED OPTIONS
    # -----------------------------
    result = {"difficulty": None, "minigun" : False, "tank" : False}  # False = normal, True = hard

    # -----------------------------
    # COLOR HANDLING
    # -----------------------------
    def set_player_color(color_name):
        official_main.player.color = color_name

    def set_outline_color(color_name):
        official_main.player.outline = color_name

    # -----------------------------
    # GAME CONTROL
    # -----------------------------
    def launch_easy():
        result["difficulty"] = False
        root.destroy()



    def launch_hard():
        result["difficulty"] = True
        root.destroy()

    def unpause_game():
        if not constants.PAUSED:
            return
        constants.PAUSED = False
        root.destroy()
        return


    def exit_game():
        pygame.quit()
        sys.exit()
    def launch_minigun():
        result["difficulty"] = False
        result["minigun"] = True
        root.destroy()
    def launch_tank():
        result["difficulty"] = False
        result["tank"] = True
        root.destroy()

    # -----------------------------
    # BACKGROUND IMAGE
    # -----------------------------
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    bg_path = os.path.join(base_path, "assets", "Background.png")
    bg_image = tk.PhotoImage(file=bg_path)

    canvas = tk.Canvas(root, width=1280, height=720, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_image)

    # -----------------------------
    # MENU BUTTONS
    # -----------------------------
    if not constants.PAUSED:
        # -----------------------------
        # NON-PAUSE MENU
        # -----------------------------
        # Title
        canvas.create_text(
            640, 60,
            text="ASTEROIDS",
            font=("Sans Serif", 48, "bold"),
            fill="white"
        )
        canvas.create_text(
            640, 344,
            text=f"Your highest score is {high_score}",
            font=("Sans Serif", 24, "bold"),
            fill="white"
        )

        # Launch Buttons
        canvas.create_window(640, 150, window=tk.Button(
            root,
            text="Press to launch normal mode",
            bg="green",
            fg="white",
            font=("Sans Serif", 20, "bold"),
            width=24,
            height=2,
            command=launch_easy
        ))

        canvas.create_window(470, 250, window=tk.Button(
            root,
            text="Press to launch hard mode",
            bg="red",
            fg="white",
            font=("Sans Serif", 18, "bold"),
            width=22,
            height=2,
            command=launch_hard
        ))
        canvas.create_window(640, 700, window=tk.Button(
            root,
            text="Press to launch minigun mode (high scores disabled)",
            bg="green",
            fg="white",
            font=("Sans Serif", 7, "bold"),
            width=40,
            height=3,
            command=launch_minigun))
        canvas.create_window(820, 250, window=tk.Button(
            root,
            text="Press to launch Tank mode",
            bg="orange",
            fg="white",
            font=("Sans Serif", 18, "bold"),
            width=22,
            height=2,
            command=launch_tank))

    else:
        # -----------------------------
        # PAUSE MENU (untouched)
        # -----------------------------
        canvas.create_text(
            640, 100,
            text="PAUSE MENU",
            font=("Sans Serif", 36, "bold"),
            fill="white"
        )

        canvas.create_window(640, 200, window=tk.Button(
            root,
            text="UNPAUSE",
            bg="green",
            fg="white",
            font=("Sans Serif", 24, "bold"),
            width=18,
            height=2,
            command=unpause_game
        ))

        canvas.create_window(640, 320, window=tk.Button(
            root,
            text="EXIT",
            bg="red",
            fg="white",
            font=("Sans Serif", 20, "bold"),
            width=15,
            height=2,
            command=exit_game
        ))



    # -----------------------------
    # COLOR MENU
    # -----------------------------
    menu_frame = tk.Frame(root, bg=None, bd=0, highlightthickness=0)
    canvas.create_window(640, 500, window=menu_frame)

    for i in range(4):
        menu_frame.columnconfigure(i, weight=1)

    title_font = ("Sans Serif", 14, "bold")
    button_font = ("Sans Serif", 12)

    # Character colors
    tk.Label(
        menu_frame,
        text="Character colors",
        font=title_font,
        bg=None
    ).grid(row=0, column=0, columnspan=4, pady=(0, 10))

    colors = [
        ("Black", "black"),
        ("Red", "red"),
        ("Green", "green"),
        ("Blue", "blue")
    ]

    for col, (name, color) in enumerate(colors):
        tk.Button(
            menu_frame,
            text=name,
            bg=color,
            fg="white",
            font=button_font,
            width=12,
            height=2,
            relief="raised",
            bd=2,
            command=lambda c=color: set_player_color(c)
        ).grid(row=1, column=col, padx=10, pady=5)

    # Outline colors
    tk.Label(
        menu_frame,
        text="Outline colors",
        font=title_font,
        bg=None
    ).grid(row=2, column=0, columnspan=4, pady=(20, 10))

    for col, (name, color) in enumerate(colors):
        tk.Button(
            menu_frame,
            text=name,
            bg=color,
            fg="white",
            font=button_font,
            width=12,
            height=2,
            relief="raised",
            bd=2,
            command=lambda c=color: set_outline_color(c)
        ).grid(row=3, column=col, padx=10, pady=5)

    # -----------------------------
    # HANDLE WINDOW CLOSE
    # -----------------------------
    def on_close():
        result["difficulty"] = None
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # -----------------------------
    # RUN TKINTER LOOP
    # -----------------------------


    root.mainloop()

    return result["difficulty"], result["minigun"], result["tank"]


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    chosen_difficulty, minigun, tank = main()
    if chosen_difficulty is not None:
        official_main.main(chosen_difficulty, minigun,tank)
