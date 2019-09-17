def main():
	h= int(input("Enter height of tree:"))
	if h < 0:
		print("The tree height is invalid. Try again!")
	for i in range (h):
		print(" "*(h-i-1)+"#"*(2*i+1))
		print(" "*(h-1)+"#")

		
main()
