country = input('請輸入你所在的國家:')
age = input('請輸入年齡:')
age = int(age)
if country == '台灣': 
	if age >= 18:
		print('可以考駕照')
	else:
		print('你還不能開車')