def encryptDecrypt(input):
	key = ['K', 'C', 'Q'] #Can be any chars, and any size array
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)