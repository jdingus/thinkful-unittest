
def calculate_discount(item_cost,relative_discount,absolute_discount):
	if item_cost == 0:
		return 0
	if item_cost < 0:
		raise Exception('item_cost is negative')
	rel_amount = item_cost * (relative_discount*.01)
	sale_price = item_cost - rel_amount - absolute_discount
	if sale_price < 0:
		return 0
	return sale_price