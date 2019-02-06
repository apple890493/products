products = []
while True:
	name = input("Enter product name: ")
	if name == "X":
		break
	price = input("Enter price: ")
	products.append([name, price])
print(products)

for p in products:
	print(p[0], "is", p[1])
