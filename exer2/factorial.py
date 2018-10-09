def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)

n = int(input())
if n<0:
	print("Enter non-negative value")
else:
	print(fact(n))