# CBTCIP

# Receipt Generator

This repository contains a simple Python script to generate a receipt PDF using the `reportlab` library. The script takes a sample receipt data dictionary, formats it, and generates a PDF file with the receipt details.

## Features

- Store information including name, address, and phone number.
- Receipt details such as receipt number and date.
- List of items with description, quantity, unit price, and total price.
- Calculation of subtotal, tax, and total amount.

## Installation

To use this script, you need to install the `reportlab` library. You can install it using pip:

```bash
pip install reportlab
```

## Usage

1. Clone this repository.
2. Ensure you have the `reportlab` library installed.
3. Modify the `receipt_data` dictionary if needed.
4. Run the script to generate the receipt PDF.

### Sample receipt data

```python
receipt_data = {
    "store_name": "Pandeyji General Store",
    "address": "Dapodi, Pune City, 411012",
    "phone": "(91) 8456-7890",
    "receipt_number": "001",
    "date": "2023-07-10",
    "items": [
        {"description": "Milk", "quantity": 2, "unit_price": 10.00},
        {"description": "Cigar", "quantity": 1, "unit_price": 45.00},
        {"description": "Sanitary Pads", "quantity": 3, "unit_price": 60.00},
    ],
    "subtotal": 245.00,
    "tax": 5.50,
    "total": 250.50
}
```

### Generate PDF

The `generate_receipt_pdf` function takes the receipt data and a file path to save the PDF:

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt_pdf(receipt_data, file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Store details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 30, receipt_data["store_name"])
    c.setFont("Helvetica", 10)
    c.drawString(30, height - 50, receipt_data["address"])
    c.drawString(30, height - 65, f"Phone: {receipt_data['phone']}")

    # Receipt details
    c.drawString(30, height - 90, f"Receipt #: {receipt_data['receipt_number']}")
    c.drawString(30, height - 105, f"Date: {receipt_data['date']}")

    # Items header
    c.drawString(30, height - 130, "Description")
    c.drawString(300, height - 130, "Quantity")
    c.drawString(400, height - 130, "Unit Price")
    c.drawString(500, height - 130, "Total")

    # Items
    y = height - 145
    for item in receipt_data["items"]:
        c.drawString(30, y, item["description"])
        c.drawString(300, y, str(item["quantity"]))
        c.drawString(400, y, f"${item['unit_price']:.2f}")
        c.drawString(500, y, f"${item['quantity'] * item['unit_price']:.2f}")
        y -= 15

    # Subtotal, tax, total
    y -= 15
    c.drawString(400, y, "Subtotal")
    c.drawString(500, y, f"${receipt_data['subtotal']:.2f}")

    y -= 15
    c.drawString(400, y, "Tax")
    c.drawString(500, y, f"${receipt_data['tax']:.2f}")

    y -= 15
    c.drawString(400, y, "Total")
    c.drawString(500, y, f"${receipt_data['total']:.2f}")

    # Save PDF
    c.showPage()
    c.save()
```

Specify the file path where you want to save the PDF:

```python
file_path = "D:/Code Practice/CBTCIP/receipt.pdf"
generate_receipt_pdf(receipt_data, file_path)
```

## License

This project is not licensed.


----------------------------------------------------------------------------------------------------------------------------------------


# Rock-Paper-Scissors Game

Welcome to the Rock-Paper-Scissors game! This simple Python script allows you to play the classic game of Rock-Paper-Scissors against the computer.

### Features

- **Interactive Gameplay**: The game prompts the user to enter their choice (rock, paper, or scissors).
- **Computer Opponent**: The computer randomly selects its choice each round.
- **Result Determination**: The game determines and displays the winner of each round based on the choices made.

### How to Play

1. **Run the Script**: Execute the script in a Python environment.
2. **Enter Your Choice**: When prompted, enter your choice of rock, paper, or scissors.
3. **View Results**: The script will display both your choice and the computer's choice, then announce the result of the game (win, lose, or tie).

### Code Overview

- `get_user_choice()`: Prompts the user to enter a valid choice (rock, paper, or scissors).
- `get_computer_choice()`: Randomly selects a choice for the computer.
- `determine_winner(user_choice, computer_choice)`: Determines the winner based on the rules of Rock-Paper-Scissors.
- `play_game()`: Main function to play the game, combining user input, computer choice, and result determination.

### Example Usage

```python
import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = ''
    while user_choice not in choices:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
```

### Requirements

- Python 3.x

### License

This project is not licensed.