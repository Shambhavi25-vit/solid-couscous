# solid-couscous
# SecurePass: Password Strength & Entropy Visualizer

## Project Overview
SecurePass is a cybersecurity tool designed to help users understand the mathematical strength of their passwords. Unlike standard checkers that only look at length, SecurePass calculates **Shannon Entropy** (in bits) and estimates the time required for a modern GPU to brute-force the password.

## Features
* **Entropy Calculation:** Uses Information Theory to calculate the exact randomness of a password string.
* **Dictionary Attack Prevention:** Instantly flags passwords found in common "Blacklists" (e.g., `password`, `123456`).
* **Visual Feedback:** Provides a color-coded bar chart representing password strength.
* **Time-to-Crack Estimation:** Calculates how long it would take to crack the password based on 100 Billion hashes/second.

## Technologies Used
* **Language:** Python 3
* **Modules:** `math`, `os` (Standard Library)
* **Concepts:** Shannon Entropy, Brute-force Math, File I/O

## How to Run
1.  Ensure you have Python installed.
2.  Clone this repository or download the files.
3.  Navigate to the project folder in your terminal.
4.  Run the main script:
    ```bash
    python src/main.py
    ```

## Testing Instructions
* **Test Weak Password:** Enter `password` or `123456`.
    * *Expected Result:* Warning message "DANGER: Found in blacklist".
* **Test Medium Password:** Enter `cat` or `dog`.
    * *Expected Result:* Low entropy score, Red/Yellow bar, "Instantly" crack time.
* **Test Strong Password:** Enter `MyS3cur3P@ssw0rd!!`.
    * *Expected Result:* High entropy score (green bar), crack time in years.

## Screenshots
**
