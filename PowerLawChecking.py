import pandas as pd
import numpy as np
import powerlaw as pl
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    # Hidden root window for dialogs
    root = tk.Tk()
    root.withdraw()

    # Ask user to select CSV file
    file_path = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        return

    # Load CSV
    df = pd.read_csv(file_path)

    results_list = []
    for col in df.columns:
        try:
            # Only analyze numeric data
            if not pd.api.types.is_numeric_dtype(df[col]):
                continue

            DATA = np.array(df[col].dropna().tolist())
            DATA = DATA[DATA > 0]  # filter nonpositive values

            fit = pl.Fit(DATA)
            alpha = fit.power_law.alpha
            xmin = fit.power_law.xmin
            R, p = fit.distribution_compare('power_law', 'lognormal')

            results_list.append({
                "Column": col,
                "alpha": alpha,
                "xmin": xmin,
                "R": R,
                "p": p
            })
        except Exception as e:
            results_list.append({
                "Column": col,
                "alpha": None,
                "xmin": None,
                "R": None,
                "p": None,
                "Error": str(e)
            })

    # Save results to Excel
    out_df = pd.DataFrame(results_list)
    out_file = file_path.replace(".csv", "_powerlaw_analysis_results.xlsx")
    out_df.to_excel(out_file, index=False)

    messagebox.showinfo("Done", f"Analysis complete!\nResults saved to:\n{out_file}")



def simple_input(prompt, root):                             #Popup input box for text entry.
    win = tk.Toplevel(root)
    win.title("Input")
    tk.Label(win, text=prompt).pack(pady=5)
    entry = tk.Entry(win, width=30)
    entry.pack(pady=5)
    entry.focus()
    result = {"value": None}

    def submit():
        result["value"] = entry.get()
        win.destroy()

    tk.Button(win, text="OK", command=submit).pack(pady=5)
    root.wait_window(win)
    return result["value"]

if __name__ == "__main__":
    main()
