# PowerLaw-Verifier
A simple power law/lognormal verifying application for data analysis. Personally used for synaptic release data analysis.



## Features
- GUI interface with **Browse** button for selecting .csv file
- Automatic statistical analysis using the `powerlaw` library
- Support multiple distribution fitting mode
- Results exported to Excel(.xlsx)



## Requirements
- Python 3.9+  
- Libraries:
  - pandas
  - numpy
  - powerlaw
  - openpyxl
  - tkinter (bundled with Python)
 
Install dependencies with:
```bash
pip install pandas numpy powerlaw openpyxl
```

## How to use
<img width="344" height="226" alt="example" src="https://github.com/user-attachments/assets/8a40943e-26c3-4f72-b4e8-2c32fede4bb9" />

Figure 1. Example format of input .csv file

1. Structure the .csv file as accordingly(Fig.1)
2. Enter Xmin value (leaving it blank will use the defualt Xmin fitting function)
3. Select and analyse the .csv using Browse
4. Check your result, the resilt file is generated as .xlsx in the same directory as the selected .csv file
