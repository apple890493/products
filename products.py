#總說明請看write.py
#*[refactor(重構程式;設計程式碼架構) 把程式碼寫成function]

#[預先檢查檔案存否]
import os 

#[讀取檔案]
def read_file(filename):#使用參數不寫死可以讀多個檔案
	products = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	return products

#[讓使用者輸入]
def user_input(products):
	while True:
		name = input("Enter product name: ")
		if name == "X":
			break
		price = input("Enter price: ")
		products.append([name, price])
	print(products)
	return products

#[印出所有購買紀錄]
def print_products(products):
	for p in products:
		print(p[0], "is", p[1])
#沒有改變任何東西(新增等),只是單純印出東西;只需要傳遞進去不須回傳

# [寫入檔案]
def write_file(filename, products):
	with open(filename, "w", encoding="utf-8") as f:
		f.write("商品,價格\n")
		for p in products:
			f.write(p[0] + "," + p[1] + "\n")
#因為只是寫到檔案而已,所以不須回傳東西



#呼叫function(這邊真正開始執行程式;上面都是定義而已)
#有return,function的執行結果就可以存下來開
def main():#主要function為程式進入點
	filename = "products.csv"
	if os.path.isfile(filename):#[檢查檔案存否]但因為只檢查一次不需要使用function
		print("Yes!")
		products = read_file(filename)#products.csv會傳到(filename)
	else:
		print("Sorry! Can't find it.")
	products = user_input(products)
	#把(products)傳進去,執行完後又存回products裡面取代原本的資料
	print_products(products)
	write_file("products.csv", products)

main()