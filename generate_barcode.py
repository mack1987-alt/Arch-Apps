import barcode
from barcode.writer import ImageWriter

# Set the barcode type and data
barcode_type = 'ean13'
data = input("Enter the code to generate barcode: ")

# Create the barcode object
my_barcode = barcode.get_barcode_class(barcode_type)(data, writer=ImageWriter())

# Save the barcode image
filename = f"generated_{barcode_type}_{data}.png"