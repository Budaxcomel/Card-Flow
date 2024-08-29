from isvalid import is_valid_credit_card
import random

def generate_valid_cc(bin_number=None):
    if bin_number is None:
        bin_number = 380000

    # Generate a random 9-digit number
    generated_num = random.randint(1_000_000_000, 9_999_999_999)
    
    # Concatenate BIN and generated number to form the card number
    card_number = str(bin_number) + str(generated_num)
    
    # Ensure that the card number is a valid credit card number
    if is_valid_credit_card(int(card_number)):
        return card_number
    else:
        return False
