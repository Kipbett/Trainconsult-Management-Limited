import random
import string

def generate_random_string(length):
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits

    # Generate a random string of the given length
    unique_id = ''.join(random.choice(characters) for i in range(length))

    return unique_id

# Example usage: generate a random string with 10 characters
random_string = generate_random_string(20)
print(random_string)