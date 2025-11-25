import os

def load_common_passwords():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'data', 'common_passwords.txt')
    
    bad_passwords = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                bad_passwords.add(line.strip().lower())
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
        
    return bad_passwords

def check_security(password, bad_passwords_set):
    if password.lower() in bad_passwords_set:
        return False
    return True