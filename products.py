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

with open("products.csv", "w",  encoding="utf-8") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")

