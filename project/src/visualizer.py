def display_bar(entropy):
    max_score = 100
    bar_length = 30
    filled_length = int((entropy / max_score) * bar_length)
    
    if filled_length > bar_length:
        filled_length = bar_length

    if entropy < 40:
        strength_text = "WEAK"
    elif entropy < 70:
        strength_text = "MEDIUM"
    else:
        strength_text = "STRONG"

    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    print(f"\nEntropy Score: {entropy} bits")
    print(f"Strength:      [{bar}] ({strength_text})")

def time_to_crack(entropy):
    guesses_per_second = 100_000_000_000
    total_combinations = 2 ** entropy
    seconds = total_combinations / guesses_per_second
    
    print("Time to Crack: ", end="")
    
    if seconds < 1:
        print("Instantly!")
    elif seconds < 3600:
        print(f"{round(seconds/60, 2)} minutes")
    elif seconds < 31536000:
        print(f"{round(seconds/86400, 2)} days")
    else:
        print(f"{round(seconds/31536000, 2)} years")
    print("-" * 50)