purchase = float(input('enter the purchase '))
discount = 0
catagory = ""
if purchase >10000:
	discount= (purchase * 20) / 100
	catagory = "vip"
elif purchase >5000:
	discount= (purchase * 10) / 100
	catagory = "gold"
	
elif purchase >2000:
	discount= (purchase * 5) / 100
	catagory = "selver"
	
elif purchase <= 2000:
	discount= (purchase * 0) / 100
	catagory = "standard"
	
else:
	print("you entered invalid keyword")
	
print(f"your discount is {discount}, and your catagori is catagory is {catagory} ")