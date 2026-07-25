import tkinter as tk
from tkinter import filedialog, messagebox
from analysis import run_analysis
import os

# List of distributions supported by powerlaw
DISTRIBUTIONS = [
    "power_law",
    "lognormal",
    "exponential",
    "truncated_power_law",
    "stretched_exponential"
]

def show_third_party_notices(root):
    parent_folder = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(parent_folder, "doc", "Third-Party Software Notices.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            notices_text = f.read()
    except Exception as e:
        notices_text = f"Error loading notices file:\n{e}"

    notice_win = tk.Toplevel(root)
    notice_win.title("Third-Party Notices")

    text = tk.Text(notice_win, wrap="word", width=80, height=25)
    text.insert("1.0", notices_text)
    text.config(state="disabled")
    text.pack(expand=True, fill="both")

def browse_file(xmin_entry, left_var, right_var):
    file_path = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if file_path:
        xmin_value = xmin_entry.get().strip()
        xmin_value = float(xmin_value) if xmin_value else None

        dist_left = left_var.get()
        dist_right = right_var.get()

        # Prevent comparing the same distribution
        if dist_left == dist_right:
            messagebox.showerror("Error", "Comparing the same distribution is not allowed. Please select different distributions.")
            return

        out_file = run_analysis(file_path, xmin=xmin_value,
                                dist_left=dist_left, dist_right=dist_right)
        messagebox.showinfo("Done", f"Analysis complete!\nResults saved to:\n{out_file}")

def main():
    root = tk.Tk()
    root.title("Distribution Comparison Tool")

    # xmin input
    tk.Label(root, text="xmin:").pack(pady=5)
    xmin_entry = tk.Entry(root)
    xmin_entry.pack(pady=5)

    # Left distribution dropdown
    tk.Label(root, text="Left Distribution:").pack(pady=5)
    left_var = tk.StringVar(value=DISTRIBUTIONS[0])
    left_menu = tk.OptionMenu(root, left_var, *DISTRIBUTIONS)
    left_menu.pack(pady=5)

    # Right distribution dropdown
    tk.Label(root, text="Right Distribution:").pack(pady=5)
    right_var = tk.StringVar(value=DISTRIBUTIONS[1])
    right_menu = tk.OptionMenu(root, right_var, *DISTRIBUTIONS)
    right_menu.pack(pady=5)

    # Browse button
    browse_btn = tk.Button(root, text="Browse CSV",
                           command=lambda: browse_file(xmin_entry, left_var, right_var))
    browse_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
