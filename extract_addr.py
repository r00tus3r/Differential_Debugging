
f = open("log.txt", "r")
a = f.readlines()
b = []

for i in a:
	for j in i.split():
		b.append(j)

f = open("trace.txt", "w")
for i in b:
	if '0x7f' in i:
		f.write(i + '\n')
