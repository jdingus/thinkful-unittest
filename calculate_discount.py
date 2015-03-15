

def calculate_discount(item_cost,relative_discount,absolute_discount):
	rel_amount = item_cost * (relative_discount*.01)
	sale_price = item_cost - rel_amount - absolute_discount
	return sale_price

print calculate_discount(200,10,30)