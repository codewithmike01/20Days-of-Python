# Install python barcode
# pip install python-barcode

# Europian satndard barcode
from barcode import EAN13

# Generate barcode as image format
from barcode.writer import ImageWriter

num_of_barcodes = int(input('How many barcodes to generate '))


for count in range(num_of_barcodes):
    id = input("Give 12 digits to convert to barcode ")
    my_bar = EAN13(id, writer=ImageWriter())
    bar_name = input("Enter the name of this bar code ")
    my_bar.save(bar_name)






