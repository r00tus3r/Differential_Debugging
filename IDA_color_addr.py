
f = open("trace", "r")
addr = f.readlines()

for i in addr:
     SetColor(int(i, 16), CIC_ITEM, 0x0000ff)
