# square_root.py
import math
import cmath  # For handling complex square roots

def find_square_root(number):
    """
    Returns the square root of a number.
    Uses math.sqrt for non-negative numbers and cmath.sqrt for negatives.
    """
    if number >= 0:
        return math.sqrt(number)  # Real square root
    else:
        return cmath.sqrt(number)  # Complex square root

def main():
    try:
        # Take user input
        user_input = input("Enter a number to find its square root: ").strip()
        
        # Convert to float (supports decimals)
        num = float(user_input)
        
        # Calculate square root
        result = find_square_root(num)
        
        print(f"The square root of {num} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()


