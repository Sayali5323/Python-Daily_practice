import re

message="Order ORD-1024 shipped. Order ORD-2048 pending.Invalid ORD-77."
order_ids=re.findall(r"ORD-\d{4}",message)#ORD- Exact text ORD- ,\d any digit from 0 to 9,{4} Exactly four digits
print(order_ids)