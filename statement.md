# SecurePass: Password Strength & Entropy Visualizer


## 1. Project Overview
*SecurePass* is a sophisticated command-line cybersecurity tool designed to audit password security. Unlike standard web-based checkers that rely on arbitrary rules (e.g., "must have 1 symbol"), SecurePass employs *Information Theory* to calculate the bit-strength of a password. It provides users with a realistic assessment of how safe their credentials are against modern brute-force attacks and offers AI-logic-based suggestions for improvement.

---

## 2. Problem Statement
In the modern digital landscape, the password remains the primary line of defense for user accounts. However, a significant disconnect exists between what users think is secure and what is mathematically secure.
* *Predictability:* Users often rely on patterns (e.g., Summer2025!, Password123) that are easily guessed by dictionary attacks.
* *False Security:* Traditional tools mark P@ssword1 as "Strong" because it meets complexity requirements, despite it being top of the list for hackers.
* *Lack of Education:* Users rarely understand the concept of "Entropy" or why adding length is exponentially better than adding complexity.

## 3. Scope of the Project
*SecurePass* is designed to bridge the gap between user perception and mathematical security reality.
*The scope encompasses:*
* *Input Validation:* Securely handling user input and validating it against a local database of compromised credentials.
* *Mathematical Rigor:* Applying *Shannon Entropy* to quantify randomness in bits, providing a scientific "Strength Score."
* *Educational Feedback:* Visualizing data to help users understand why a password is weak and providing actionable, algorithmic steps to improve it.
* *Platform Independence:* A lightweight CLI utility that runs efficiently on any system with Python installed, ensuring accessibility.

## 4. Target Users
* *General Users:* Individuals wishing to audit their personal passwords against mathematical rigor rather than arbitrary rules.
* *System Administrators:* IT professionals looking to demonstrate the importance of password policies (length vs. complexity) to employees.
* *Cybersecurity Students:* Learners who need to visualize concepts of Information Theory, Combinatorics, and Brute-force logic in a practical application.

---

## 5. High-Level Features
### 🔐 Core Security Engine
* *Entropy Calculation:* Calculates the exact randomness of a password using the formula $E = L \times \log_2(R)$.
* *Blacklist Defense:* Instantly detects and blocks passwords found in common breach dictionaries (e.g., password, 123456, admin).
* *Smart Suggestions:* Analyzes weak passwords and algorithmically generates a stronger, memorable version (e.g., transforming apple into ApPl3@9).

### 📊 Visualization & Analytics
* *Dynamic Strength Bar:* A color-coded, real-time loading bar that visualizes the "Bit Strength" of the input.
* *Time-to-Crack Estimation:* Estimates how long a modern GPU (RTX 4090 hash rate) would take to brute-force the password, converting abstract math into tangible time (e.g., "300 Years").
* *Secure Input Mode:* Hides characters while typing to prevent "shoulder surfing" attacks.

---

## 6. Technical Architecture
The project follows a *Modular Architecture* to ensure clean code and easy maintenance.

```text
SecurePass_Project/
│
├── data/
│   └── common_passwords.txt    # Database: Contains 10,000+ most common weak passwords.
│
├── src/
│   ├── main.py                 # Controller: Handles user interaction and workflow logic.
│   ├── entropy.py              # Math Module: Calculates Shannon Entropy and generates suggestions.
│   ├── validator.py            # Security Module: Handles file I/O and blacklist verification.
│   └── visualizer.py           # UI Module: Generates ASCII bar charts and formats output.
│
└── README.md                   # Documentation
