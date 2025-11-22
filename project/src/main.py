import entropy
import validator
import visualizer

def main():
    print("============================================")
    print("    VITyarthi SecurePass Visualizer v1.0    ")
    print("============================================")
    
    blacklist = validator.load_common_passwords()
    
    while True:
        user_pass = input("\nEnter a password to test (or 'q' to quit): ")
        
        if user_pass.lower() == 'q':
            print("Exiting...")
            break
            
        is_safe = validator.check_security(user_pass, blacklist)
        
        if not is_safe:
            print("\n[!] DANGER: This password is in the common blacklist!")
            print("[!] It would be cracked instantly.")
            continue # Skip the rest and ask again
            
        score = entropy.calculate_entropy(user_pass)
        
        visualizer.display_bar(score)
        visualizer.time_to_crack(score)

if __name__ == "__main__":
    main()