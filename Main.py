import os
import tkinter as tk
from tkinter import messagebox
from ui.ui import show_third_party_notices, browse_file
import webbrowser

# List of distributions supported by powerlaw
DISTRIBUTIONS = [
    "power_law",
    "lognormal",
    "exponential",
    "truncated_power_law",
    "stretched_exponential"
]

def create_main_window():
    root = tk.Tk()
    root.title("Power Law Checker")

    # Load icon from ui folder (ICO only)
    icon_path = os.path.join(os.path.dirname(__file__), "ui", "icon.ico")
    root.iconbitmap(icon_path)

    # Window size
    window_width = 400
    window_height = 200

    # Position at cursor (centered around cursor)
    cursor_x = root.winfo_pointerx()
    cursor_y = root.winfo_pointery()
    root.geometry(f"{window_width}x{window_height}+{cursor_x}+{cursor_y}")

    # Menu bar
    menubar = tk.Menu(root)
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(
        label="GitHub",
        command=lambda: webbrowser.open("https://github.com/xXdaWeagodXx/PowerLaw-Verifier/tree/main")
    )
    help_menu.add_command(
        label="Third-Party Notices", 
        command=lambda: show_third_party_notices(root)
    )
    menubar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menubar)

    # xmin input box
    tk.Label(root, text="xmin value:").pack(pady=5)
    xmin_entry = tk.Entry(root)
    xmin_entry.pack(pady=5)


    # Comparison row
    comp_frame = tk.Frame(root)
    comp_frame.pack(pady=10)

    # "Compair" label
    tk.Label(comp_frame, text="Compair").grid(row=0, column=0, padx=5)

    # Left distribution dropdown
    left_var = tk.StringVar(value=DISTRIBUTIONS[0])
    left_menu = tk.OptionMenu(comp_frame, left_var, *DISTRIBUTIONS)
    left_menu.grid(row=0, column=1, padx=5)

    # "vs" label
    tk.Label(comp_frame, text="vs").grid(row=0, column=2, padx=5)

    # Right distribution dropdown
    right_var = tk.StringVar(value=DISTRIBUTIONS[1])
    right_menu = tk.OptionMenu(comp_frame, right_var, *DISTRIBUTIONS)
    right_menu.grid(row=0, column=3, padx=5)


    # Browse button in middle
    browse_btn = tk.Button(
        root,
        text="Browse",
        command=lambda: browse_file(xmin_entry, left_var, right_var),
        width=20,
        height=2
    )
    browse_btn.pack(pady=10)

    return root

if __name__ == "__main__":
    root = create_main_window()
    root.mainloop()
