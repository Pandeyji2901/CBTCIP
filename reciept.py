
# Sample receipt data
receipt_data = {
    "store_name": "Pandeyji General Store",
    "address": "Dapodi, Pune City, 411012",
    "phone": "(91) 8456-7890",
    "receipt_number": "001",
    "date": "2023-07-10",
    "items":
    [
        {"description": "Milk", "quantity": 2, "unit_price": 10.00},
        {"description": "Cigar", "quantity": 1, "unit_price": 45.00},
        {"description": "Sanitary Pads", "quantity": 3, "unit_price": 60.00},
        
    ],
    "subtotal": 245.00,
    "tax": 5.50,
    "total": 250.50
}


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

# File path to save the PDF
file_path = "D:\Code Practice\CBTCIP/receipt.pdf"
generate_receipt_pdf(receipt_data, file_path)
