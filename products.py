#總說明請看write.py

#[預先檢查檔案存否]
import os 

#[讀取檔案]
products = []
if os.path.isfile("products.csv"):#[檢查檔案存否]
	print("Yes!")
	with open("products.csv", "r", encoding="utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	print(products)

else:
	print("Sorry! Can't find it.")

#[讓使用者輸入]
while True:
	name = input("Enter product name: ")
	if name == "X":
		break
	price = input("Enter price: ")
	products.append([name, price])
print(products)

#[印出所有購買紀錄]
for p in products:
	print(p[0], "is", p[1])

# [寫入檔案]
with open("products.csv", "w", encoding="utf-8") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")