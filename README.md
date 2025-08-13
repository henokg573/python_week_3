# python_week_3
# Calculate Discount Program

## 📌 Description
This Python program calculates the final price of an item after applying a discount.  
It follows these rules:
- If the discount percentage is **20% or higher**, the discount is applied.
- If the discount percentage is **less than 20%**, the original price is returned.

The program:
- Prompts the user for the **original price** and **discount percentage**.
- Applies the discount only when the condition is met.
- Displays the **final price** or informs the user that no discount was applied.
- Handles invalid (non-numeric) inputs gracefully.

---

## 🛠 Features
- **Function-based structure** for clean, reusable code.
- **Docstrings and comments** to explain functionality.
- **Error handling** to avoid crashes on invalid input.
- **Formatted output** with 2 decimal places.

---

## 📂 File Structure
python.py



---

## 📋 How It Works
1. The user runs the Python file, ==> by python python.py
2. The program asks for:
   - Original price of the item.
   - Discount percentage.
3. If the discount is `>= 20%`:
   - The program calculates the discount amount.
   - The final price is obtained by subtracting the discount from the original price.
4. If the discount is `< 20%`, the original price is returned.
5. The result is displayed to the user.

---

## 💻 Usage
Run the program in a terminal or Python IDE:

```bash
python python.py

