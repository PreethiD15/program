x, y,z = map(int, input().split()) 
if((x<y)and(x<z)):
	if(y<z):
		print(z)
	else:
		print(y)
else:
	print(x)
