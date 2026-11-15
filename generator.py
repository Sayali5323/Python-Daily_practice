def running_total(sales):
    total=0
    for amount in sales:
        total=total+amount
        yield total

sales=[100,150,50,200]

for result in running_total(sales):
    print(result)