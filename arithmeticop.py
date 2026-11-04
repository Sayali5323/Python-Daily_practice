#10% discount on total bill

item=float(input("Enter the price of 1 item: "))
quantity=int(input("Enter the quantity: "))
total=item*quantity
dicount=total*10/100
final_bill=total-dicount
print("Total Bill",final_bill)
