def display_bar(entropy):
    max_score = 100
    bar_length = 20    
    filled_length = int((entropy / max_score) * bar_length)
    
    if filled_length > bar_length:
        filled_length = bar_length
        
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    print(f"\nEntropy Score: {entropy} bits")
    print(f"Strength:      [{bar}]")

def time_to_crack(entropy):
    guesses_per_second = 100_000_000_000
    
    total_combinations = 2 ** entropy
    
    seconds = total_combinations / guesses_per_second
    
    print("Time to Crack: ", end="")
    if seconds < 1:
        print("Instantly!")
    elif seconds < 60:
        print(f"{round(seconds, 2)} seconds")
    elif seconds < 3600:
        print(f"{round(seconds/60, 2)} minutes")
    elif seconds < 86400:
        print(f"{round(seconds/3600, 2)} hours")
    elif seconds < 31536000:
        print(f"{round(seconds/86400, 2)} days")
    else:
        print(f"{round(seconds/31536000, 2)} years")
    print("-" * 40)