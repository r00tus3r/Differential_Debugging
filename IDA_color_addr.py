
f = open("trace.txt", "r")
addr = f.readlines()
cnt = 0

for i in addr:
     addr[cnt] = int(i[:-1], 16)
     SetColor(addr[cnt]-0x7fff89033000, CIC_ITEM, 0x0000ff)
     cnt += 1
