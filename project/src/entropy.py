import math
import random

def calculate_entropy(password):
    pool_size = 0
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_lower: pool_size += 26
    if has_upper: pool_size += 26
    if has_digit: pool_size += 10
    if has_symbol: pool_size += 32

    if pool_size == 0:
        return 0
        
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def get_feedback(password):
    tips = []
    
    if len(password) < 12:
        tips.append("Increase length to at least 12 characters.")
    if not any(c.isupper() for c in password):
        tips.append("Add Uppercase letters (A-Z).")
    if not any(c.isdigit() for c in password):
        tips.append("Add Numbers (0-9).")
    if not any(not c.isalnum() for c in password):
        tips.append("Add Symbols (!@#$).")
        
    return tips

def suggest_improvement(password):
    chars = list(password)
    
    for i in range(len(chars)):
        if chars[i].islower() and random.choice([True, False, False]): 
            chars[i] = chars[i].upper()
            
    if not any(c.isupper() for c in chars):
        lower_idxs = [i for i, c in enumerate(chars) if c.islower()]
        if lower_idxs:
            idx = random.choice(lower_idxs)
            chars[idx] = chars[idx].upper()
            
    if not any(c.isdigit() for c in chars):
        insert_pos = random.randint(0, len(chars))
        chars.insert(insert_pos, str(random.randint(0, 9)))
    
    if random.choice([True, False]):
        insert_pos = random.randint(0, len(chars))
        chars.insert(insert_pos, str(random.randint(0, 9)))

    if not any(not c.isalnum() for c in chars):
        symbols = "!@#$%^&*"
        insert_pos = random.randint(0, len(chars))
        chars.insert(insert_pos, random.choice(symbols))
        
    return "".join(chars)