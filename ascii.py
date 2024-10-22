
def decrypt(message : [int]) -> str:
	final_message = []
	for char in message:
		final_message.append(chr(char))
	return ''.join(final_message)

if __name__ == '__main__':
	l_toDecrypt = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99, 101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101, 32, 33]
	print(decrypt(l_toDecrypt))
