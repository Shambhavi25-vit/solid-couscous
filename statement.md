# Problem Statement & Scope

## Problem Statement
Most users create passwords based on predictable patterns (names, dates, dictionary words) rather than mathematical randomness. These passwords are highly susceptible to dictionary and brute-force attacks. Users often lack an understanding of "Entropy" and why adding a single symbol can exponentially increase security.

## Scope of the Project
The project is a CLI (Command Line Interface) tool that:
1.  Accepts user input securely.
2.  Validates the input against a database of 10,000+ common weak passwords.
3.  Calculates the bit-strength (Entropy) of the string.
4.  Visualizes the data to educate the user on password hygiene.

## Target Users
* **General Users:** To test their personal passwords.
* **System Administrators:** To demonstrate password policies to employees.
* **Cybersecurity Students:** To understand the math behind brute-force attacks.

## High-Level Features
* **Input Validation:** Sanity checks and blacklist filtering.
* **Mathematical Analysis:** Implementation of the Shannon Entropy formula.
* **Reporting:** Real-time feedback on "Time to Crack."'
