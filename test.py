def fib(n):
	a, b = 0, 1
	for i in range(n):
		print(a, end=" ")
		a, b = b, a+b
		

def pattern1(n):
	for i in range(1, n+1):
		print("*" * i)

def pattern2(n):
	for i in range(1, n+1):
		print( " " * (n-i) + "*"*(2 * (i-1) + 1))

def pattern3(n):
	for i in range(1,n+1):
		print("*" * i)
	for i in range(n-1, 0, -1):
		print("*" * i)
		
def pattern4(n):
	print("*")
	for i in range(1,n-1):
		print("*" + " "* (i-1) + "*")
	print("*" * n)

fib(10)
print("\n\n")
pattern1(5)
print("\n\n")
pattern2(5)
print("\n\n")
pattern3(5)
print("\n\n")
pattern4(5)
print("\n\n")