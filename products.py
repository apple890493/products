#建立記帳程式(二維;2 dimensional )
#二維清單=清單中還有清單;比方一節車廂裏頭兩個小包廂;
#while loop 比較適合運用在不知道執行幾次的情況

products = []
while True:
	name = input("Enter product name: ")
	if name == "X":
		break
	price = input("Enter price: ")
	#p=[]
	#p.append(name)
	#p.append(price)

	#p = [name, price]為上列快速的作法
	#products.append(p)
	
	products.append([name, price])
	#為整體最快速的寫法
print(products)

#products[0][0] 為存取二為清單; 第一個數字為第0節車廂;第二個數字為車廂內第0個包廂

