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

#字串相加
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'
# with 一離開那一區間會自動close
#encoding='utf-8'
with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
	    f.write(p[0] + ',' + p[1] + '\n')