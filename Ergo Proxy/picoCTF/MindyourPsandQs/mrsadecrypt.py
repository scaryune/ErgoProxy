from cryptography.fernet import Fernet


message = "8533139361076999596208540806559574687666062896040360148742851107661304651861689"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string",  encMessage)


decMessage = fernet.decrypt(encMessage).decode()

print("decrypt string", decMessage)

