import os

#讀取檔案
def read_file():
	products = []
	if os.path.isfile('products.csv'): #檢查檔案是否存在
		print('find the document!!!')
		with open('products.csv','r',encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue # 繼續
				name, price = line.strip().split(',')
				products.append([name,price])
			print(products)
	else:
		print('找不到檔案')
		
#讓使用者輸入

def user_input():
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name,price])
	print(products)

#列印出所有購買紀錄
def print_products():
	for p in products:
		print(P[0],'的價格是:',P[1])

#寫入檔案
def write_file():
	with open('products.csv','w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
