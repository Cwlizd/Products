# 二維清單概念
products = []
total_price = []
while True:
    name = input('輸入商品名稱:')
    if name == 'q':
    	break
    price = input('商品價格為:')
    products.append([name,price])
print(products)
print(products[0][0])

for p in products:
	print('商品為',p[0],'價格為',p[1])