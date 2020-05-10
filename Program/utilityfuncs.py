import os

def encryptDecrypt(input):
	key = ['K', 'C', 'Q']
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)

def callclearscreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def callpause():
	somechar =''
	somechar = input("Enter any key to continue....")
	
def DD(a:str,b:str,c:int):
	print("UserName  : {}".format(a))
	print("Password  : {}".format(b))
	print("User Type : {}".format(c))

def MenuHeaderPrinter(title : str):
	print(title.center(80,'-'))