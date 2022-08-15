from encodings import utf_8


rfile = open('sample.txt',encoding='utf-8')
text = rfile.read()
rfile.close()
# text = text.replace('。','～♪')
print(text)