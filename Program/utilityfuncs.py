import os

def encryptDecrypt(input):
	'''
	An XOR Encryptor function to encrypt and deccrypt.
	If a string encrypted by this function is passed to this function, it returns a decrypted string and vice-versa.
	'''
	key = ['K', 'C', 'Q']
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)

def callclearscreen():
	'''
	Function to clear screen
	'''
	os.system('cls' if os.name == 'nt' else 'clear')

def callpause():
	'''
	Function to create "Enter any key to continue" on any OS.
	'''
	somechar =''
	somechar = input("Enter any key to continue....")
	
def DD(a:str,b:str,c:int):
	'''
	Function to quickly print details.
	Assumes a and b as a string, c as in integer.
	Directly prints values of a,b and c.
	'''
	print("UserName  : {}".format(a))
	print("Password  : {}".format(b))
	print("User Type : {}".format(c))

def MenuHeaderPrinter(title : str):
	'''
	Prints menu headers.
	Output is formatted in between '-' and with total length as 80 characters
	'''
	print(title.center(80,'-'))

class WrongChoiceError(Exception):
	'''
	Custom made class.
	Derived from Exception Class.
	For Wrongly chosen option in menu based system.
	'''
	pass

class BreakMenu(Exception):
	'''
	Custom made class
	Derived from Exception Class
	For Return or logout choice in menu based system
	'''
	pass