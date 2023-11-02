print('您好! 現在要計算你的BMI, 請依序輸入身高體重')

height = int(input('請問您身高多高?(cm)'))
weight = float(input('請問您體重多種?(kg)'))

height = float(height / 100)

bmi = float(weight/(height * height))


if bmi >= 18.5 and bmi < 24:
	print('正常範圍, BMI =', bmi)
elif bmi < 18.5:
	print('體重過輕, BMI =', bmi)
else:
	print('異常範圍')
	if bmi >= 24 and bmi < 27:
		print('過重, BMI =', bmi)
	elif bmi >= 27 and bmi < 30:
		print('輕度肥胖, BMI =', bmi)
	elif bmi >= 30 and bmi < 35:
		print('中度肥胖, BMI =', bmi)
	else:
		print('重度肥胖, BMI =', bmi)
