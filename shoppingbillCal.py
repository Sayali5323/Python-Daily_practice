product=input("Enter the product name: ")
price=float(input("Enter the product price:"))
quantity=int(input("Enter the quantity:"))

total=price*quantity
print("Total Bill:",total)

if total>=500:
    discount=total*10/100
else:
    discount=0

print("discount:",discount)

Finalamount=total-discount
print("Final Amount:",Finalamount)