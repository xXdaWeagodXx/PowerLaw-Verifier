import pandas as pd
import numpy as np
import powerlaw as pl

def run_analysis(file_path, dist_left='power_law', dist_right='lognormal', xmin=None):
    # Prevent comparing the same distribution
    if dist_left == dist_right:
        raise ValueError("Left and right distributions must be different.")

    df = pd.read_csv(file_path)
    results_list = []

    for col in df.columns:
        try:
            if not pd.api.types.is_numeric_dtype(df[col]):
                continue

            DATA = np.array(df[col].dropna().tolist())
            DATA = DATA[DATA > 0]

            # Fit the data
            if xmin is not None:
                fit = pl.Fit(DATA, xmin=xmin)
            else:
                fit = pl.Fit(DATA)

            # Extract parameters for power law (always available)
            alpha = fit.power_law.alpha
            xmin_used = fit.power_law.xmin

            # Compare chosen distributions
            R, p = fit.distribution_compare(dist_left, dist_right)

            results_list.append({
                "Column": col,
                "alpha": alpha,
                "xmin": xmin_used,
                "Left": dist_left,
                "Right": dist_right,
                "R": R,
                "p": p
            })
        except Exception as e:
            results_list.append({
                "Column": col,
                "alpha": None,
                "xmin": None,
                "Left": dist_left,
                "Right": dist_right,
                "R": None,
                "p": None,
                "Error": str(e)
            })

    out_df = pd.DataFrame(results_list)
    out_file = file_path.replace(".csv", "_distribution_comparison_results.xlsx")
    out_df.to_excel(out_file, index=False)
    return out_file
