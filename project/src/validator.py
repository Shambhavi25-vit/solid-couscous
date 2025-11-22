import os

def load_common_passwords():
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'data', 'common_passwords.txt')
    
    bad_passwords = set()
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                  bad_passwords.add(line.strip())
    except FileNotFoundError:
        print("Error: common_passwords.txt not found!")
        
    return bad_passwords

def check_security(password, bad_passwords_set):
    
    if password in bad_passwords_set:
        return False 
    return True