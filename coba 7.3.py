h = ('pagi', 'siang', 'sore', 'petang', 'malam')
n = input ('masukkan nama;')
p = float (input ('pukul berapa sekarang?) (format 24 jam):'))
if  p>1.00 and p<10.59:
    p = h[0]
elif p>= 11.00 and p<=14.59:
    p = h[1]
elif p>= 15.00 and p<=16.30:
    p = h[2]
elif p>= 16.31 and p<=18.59:
    p = h[3]
elif p>=19.00 and p<=24.59:
    p = h[4]
print ('''selamat%s%s.'''  %  (p,n))
