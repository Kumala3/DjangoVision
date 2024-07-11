import random
import string


def generate_secret_key(length: int) -> str:
    """
    Generates a secret key with a specified length
    """
    # Combine ASCII letters, digits, and punctuation sings to form the character pool
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate the secret key by randomly selecting characters from the pool
    secret_key = "".join(random.choice(chars) for _ in range(length))
    return secret_key


if __name__ == "__main__":
    # Example usage: Generate and print a 40-character long secret key
    print(generate_secret_key(40))
