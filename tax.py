TAX_RATE = 0.06

def salesTax(subTotal):
    salesTax = round((subTotal * TAX_RATE), 2)
    return salesTax

def grandTotal(subTotal, salesTax):
    grandTotal = round((subTotal + salesTax), 2)
    return grandTotal