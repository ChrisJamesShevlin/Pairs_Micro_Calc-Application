import tkinter as tk
from tkinter import ttk

# Fixed margin requirements for each ETF
MARGIN_REQUIREMENTS = {
    "US500": 300,
    "US30": 2242,
    "NAS": 1044,
}

# Fixed maximum stakes for ETF2 based on its selection
MAX_STAKE = {
    "US30": 0.01,
    "NAS": 0.02,
}

def calculate_stake():
    try:
        # Get input values
        etf1_price = float(etf1_entry.get())
        etf2_price = float(etf2_entry.get())
        
        # Get selected ETFs and their margins
        etf1_name = etf1_combobox.get()
        etf2_name = etf2_combobox.get()
        etf1_margin = MARGIN_REQUIREMENTS[etf1_name]
        
        # Get the fixed maximum stake for ETF2
        etf2_stake = MAX_STAKE[etf2_name]
        
        # Calculate the required stake per point for ETF1 to balance monetary exposure
        etf1_stake = round(etf2_stake * (etf2_price / etf1_price), 2)
        
        # Display the results
        result_label.config(
            text=f"To balance:\n"
                 f"ETF1 ({etf1_name}) stake per point = £{etf1_stake}\n"
                 f"ETF2 ({etf2_name}) stake per point = £{etf2_stake}\n"
                 f"(Max stake for ETF2 applied: £{etf2_stake})"
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")
    except KeyError:
        result_label.config(text="Please select valid ETFs.")

# Set up main window
root = tk.Tk()
root.title("Spread Bet Pairs Trade Calculator")
root.geometry("500x500")

# Set dark theme with bright blue text
root.configure(bg='#1e1e1e')
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", foreground="#00bfff", background="#1e1e1e")
style.configure("TButton", foreground="#00bfff", background="#3e3e3e")
style.configure("TEntry", foreground="#00bfff", background="#1e1e1e", fieldbackground="#3e3e3e")
style.configure("TCombobox", foreground="#00bfff", background="#3e3e3e")

# ETF selection
etf1_label = ttk.Label(root, text="Select ETF1:")
etf1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
etf1_combobox = ttk.Combobox(root, values=list(MARGIN_REQUIREMENTS.keys()), state="readonly")
etf1_combobox.grid(row=0, column=1, padx=10, pady=5)

etf2_label = ttk.Label(root, text="Select ETF2:")
etf2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
etf2_combobox = ttk.Combobox(root, values=["US30", "NAS"], state="readonly")
etf2_combobox.grid(row=1, column=1, padx=10, pady=5)

# Input labels and entries
etf1_price_label = ttk.Label(root, text="ETF1 Price per Share:")
etf1_price_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
etf1_entry = ttk.Entry(root)
etf1_entry.grid(row=2, column=1, padx=10, pady=5)

etf2_price_label = ttk.Label(root, text="ETF2 Price per Share:")
etf2_price_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
etf2_entry = ttk.Entry(root)
etf2_entry.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_stake)
calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Result display
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2)

# Center the window
root.eval('tk::PlaceWindow . center')

# Run the application
root.mainloop()
