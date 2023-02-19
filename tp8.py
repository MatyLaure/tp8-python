f = open('TP8.txt', 'w')
f.write ('Primera linea del archivo TP8\n')
f.close

f = open('TP8.txt', 'r+')
f.readline()
f.write ('Segunda linea del ficheron TP8\n')
f.close

print(f.read())
f.close