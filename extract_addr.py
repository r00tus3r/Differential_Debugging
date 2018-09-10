
f = open("out", "r")
data = f.readlines()
w = open("trace", "w")

for i in data:
    for j in i.split():
        if '0x4' in j:
            try:
                int(j.strip(':'), 16)
            except:
                continue
            w.write(j.strip(':') + '\n')
