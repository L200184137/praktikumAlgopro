##activity 1
file = open('nadhifah','w')
file.write('L200184137'+'/n')
file.write(' '+'/n')
file.write('nadhifah chairunnisa'+'/n')
file.write(' '+'/n')
file.write('20-08-2000'+'/n')
file.close()


##activty 2
newFile = open('L200184137','r')
NIM = newFile.readline()
TTL = newFile.readline()
NAME = newFile.readline()
newFile.close()

import shelve
newFile1 = shelve.open('L200184137.data')
newFile1 ['data'] = [NIM, TTL, NAME]
newFile1.close()

##activity 3
import shelve
newFile2 = shelve.open('nadhifah.data')
for i in newFile2 ['data']:
    print (i),
newFile2.close()


##activity 4
import shelve
newFile3 = shelve.open('L200184137.data')
for k in newFile3['data']:
    print (k),
newFile3.close()
