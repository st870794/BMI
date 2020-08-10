tall = input('請輸入您的身高(公分):')
weight = input('請輸入您的體重(公斤)：')
tall = float(tall)
weight = float(weight)
BMI=(weight/(tall*0.01)**2)
print('您的BMI值為:',BMI)
if BMI <= 18.5:
	print('有點太輕了，多吃點!!')
elif BMI >= 24 and BMI < 27:
	print('些許過重，請記得有空多運動')
elif BMI >= 27 and BMI < 30:
	print('確定要繼續胖下去??')
elif BMI >=30:
	print('跟你沒什麼好說的，胖子')
else:
	print('很好，繼續保持體魄!')