Here’s a plain text README for your project:

---

# Spread Bet Pairs Trade Calculator

A simple GUI application built with Python and Tkinter to calculate the stake per point for balancing spread bets between two ETFs (Exchange-Traded Funds). The calculator ensures fixed maximum stakes for ETF2:

- US30: £0.01 per point
- NAS: £0.02 per point

---

## Features

- Allows selection of two ETFs (ETF1 and ETF2) and their prices.
- Automatically calculates the required stake per point for ETF1 to balance monetary exposure.
- Ensures fixed maximum stakes for ETF2.
- Modern dark-themed GUI with bright blue text.

---

## Requirements

- Python 3.7 or higher
- Tkinter (pre-installed with Python)

---

## Installation

1. Clone the repository to your local machine:
   `git clone https://github.com/your-username/spread-bet-calculator.git`
2. Navigate to the project directory:
   `cd spread-bet-calculator`
3. Run the application:
   `python calculator.py`

---

## Usage

1. Open the application.
2. Select **ETF1** and **ETF2** from the dropdown menus.
3. Input the price per share for each ETF.
4. Click the "Calculate" button to get the results.
5. The application will display:
   - The calculated stake per point for ETF1.
   - The fixed stake per point for ETF2 (based on predefined maximums).

---

## Example

If ETF1 is **US500** with a price of £4500 and ETF2 is **NAS** with a price of £15500:
- ETF2 stake will always be £0.02 (fixed maximum for NAS).
- The application will calculate the proportional stake for ETF1.

- ![image](https://github.com/user-attachments/assets/7b3fa93d-c8d1-4fb5-bf42-7e9d4a43f3a9)


---

## Fixed Parameters

### Margin Requirements (per ETF):
- US500: £300
- US30: £2242
- NAS: £1044

### Maximum Stakes for ETF2:
- US30: £0.01
- NAS: £0.02

---

## Customization

To modify ETF lists or adjust parameters:
- Edit the `MARGIN_REQUIREMENTS` dictionary in the code to change margin values.
- Edit the `MAX_STAKE` dictionary to update maximum stakes for ETF2.

---

## Contributing

Contributions are welcome! Feel free to share improvements or new features.

---



