repeat = True
n = 2
while repeat:
    x = input('masukkan password:')
    if x == 'dhifaa':
        repeat = False
        print ('anda berhasil login')
    elif x!='dhifaa':
        repeat = True
        if n !=0:
            print ('maaf, anda salah memasukkan password.')
            n=n-1
        else:
            print ('anda sudah mencoba 3kali. Akses anda ditolak')
            break
