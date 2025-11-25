import entropy
import validator
import visualizer

def main():
    print("============================================")
    print("    VITyarthi SecurePass Visualizer v2.0    ")
    print("============================================")
    
    blacklist = validator.load_common_passwords()
    
    while True:
        try:
            user_pass = input("\nEnter a password to test (or 'q' to quit): ")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        
        if user_pass == "" or user_pass.lower() == 'q':
            print("Exiting...")
            break
            
        is_safe = validator.check_security(user_pass, blacklist)
        
        if not is_safe:
            print("\n[!] DANGER: This password is in the common blacklist!")
            print("[!] It would be cracked instantly.")
            continue
            
        score = entropy.calculate_entropy(user_pass)
        
        if hasattr(entropy, 'get_feedback'):
            tips = entropy.get_feedback(user_pass)
            if tips:
                print("\nSuggestions to improve:")
                for tip in tips:
                    print(tip)
            
            if hasattr(entropy, 'suggest_improvement'):
                better_pass = entropy.suggest_improvement(user_pass)
                print(f"\nSuggested Password: {better_pass}")
        
        visualizer.display_bar(score)
        visualizer.time_to_crack(score)

if __name__ == "__main__":
    main()