a = b'r\xc3\xa9sum\xc3\xa9'
a_decode = a.decode()
print(a_decode)
b_latin1= a_decode.encode('Latin1')
print(b_latin1)
b_latin1_decode = b_latin1.decode('Latin1')
print(b_latin1_decode)
