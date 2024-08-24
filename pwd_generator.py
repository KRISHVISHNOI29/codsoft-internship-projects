import random
import string

def generate_password(length=12):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password(11)  # Generate a 16-character password
print("Generated Password:", password)
