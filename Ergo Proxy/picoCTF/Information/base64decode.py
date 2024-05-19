# importing the module
import base64

#assigning our samples to a variable
convertsample = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"

#converting the base64 code into ascii characters
convertbytes = convertsample.encode("ascii")

#converting into bytes from base64 system

convertedbytes = base64.b64decode(convertbytes)


#decoding the ASCII characters into alphabets

decodedsample = convertedbytes.decode("ascii")

#displaying the result

print(f"The string after decoding is: {decodedsample}")

