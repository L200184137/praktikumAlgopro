from datetime import datetime
import time
print ('program menampilkan waktu komputer')
while int(datetime(). strftime('%S'))>0:
    print (datetime.now().strftime('%H:%M:%S'))
    int (datetime.now().strftime('%S'))
    time.sleep(1)
print ('jam praktikum sudah habis. silahkan pulang.')


print (datetime.now())

import time
print ('program menampilkan waktu komputer')
a = time.localtime()
detik = -1
while detik !=0:
    jam = a.tm_hour
    menit = a.tm_min
    detik = a.tm_sec
    b = time.localtime()
    print("%S:%S:%S"%(jam, menit, detik))
while b==a:
    b = time.localtime()
    a=b
    print('waktu praktikum telah habis')
    
