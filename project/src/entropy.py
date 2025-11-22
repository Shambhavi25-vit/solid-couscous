import math

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