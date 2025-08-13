# by Henok Girma, August 13th 2025
# Function: calculate_discount
# Purpose: Calculates the final price of an item after applying a discount
# Parameters:
#   price (float) - The original price of the item
#   discount_percent (float) - The discount percentage to apply
# Logic:
#   If the discount percentage is 20% or higher, the discount is applied.
#   Otherwise, the original price is returned without changes.
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage.

    Returns:
        float: Final price after discount if applicable, 
               otherwise the original price.
    """
    # Check if discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# ---- MAIN PROGRAM ----

# Ask the user for the original price
try:
    original_price = float(input("Enter the original price of the item: "))
    
    # Ask the user for the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Call the function to get the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display results based on whether discount was applied
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")

# Handle invalid inputs (e.g., text instead of numbers)
except ValueError:
    print("Error: Please enter valid numeric values for price and discount.")
