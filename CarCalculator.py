# Car Price Calculator

def title():
    print("Car Price Calculator\n")

def main():
    title()
    makeModel = input("Enter car make and model: ")
    price = float(input("Enter car price: $"))
    hstRate = float(input("Enter HST rate (%): "))
    
    pdi = calculatePDI(price)
    tax = calculateTax(price, hstRate)
    total = price + pdi + tax
    
    displayInvoice(makeModel, price, pdi, tax, total, hstRate)

def calculatePDI(price):
    return price * 0.02

def calculateTax(price, hstRate):
    return price * (hstRate / 100.0)

def displayInvoice(makeModel, price, pdi, tax, total, hstRate):
    print("\n" + "=" * 40)
    print(f"Invoice for: {makeModel}")
    print("=" * 40)
    print(f"Base Car Price: ${price:.2f}")
    print(f"PDI (2%):       ${pdi:.2f}")
    print(f"HST ({hstRate}%):    ${tax:.2f}")
    print("-" * 40)
    print(f"Total:          ${total:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()





