Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = 'nadhifah chairunnisa'
>>> NIM = 137
>>> height = 1.57

>>> weight = 55
>>> yearOfBirth = 2000
>>> me = (yearOfBirth, weight, height, NIM, name)
>>> data = [yearOfBirth, weight, height, NIM, name]
>>> type (me)
<class 'tuple'>
>>> ##because it uses parentheses () and each element is written sequentially with as a separator
>>> me[0]
2000
>>> ##because me [0] shows the index one, and the index one is YearOfBirth
>>> a = NIM%4; me[a]
55
>>> ##because me[a] shows the second index, and the second index is weight
>>> type (me[a])
<class 'int'>
>>> ##because me [a] shows the weight which is an integer, 55
>>> me [a:4]
(55, 1.57, 137)
>>> ## because me[a:4] show from the second index to fourth index
>>> type (me[4])
<class 'str'>
>>> ##because me [4] shows the fifth index is name and in the fifth index there are strings and letters more than one word
>>> me[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    me[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ##because it shows the tuple class, and the tuple class cannot be changed
>>> type(data)
<class 'list'>
>>> ##list and tuple are the same but the only difference is parentheses, tuple uses () and lists use []
>>> type(data[4])
<class 'str'>
>>> ##because me [4] shows the fifth index is name and in the fifth index there are strings and letters more than one word
>>> data[4][5]
'f'
>>>  ##because the fourth index of data is name and the fifth row of name is f
>>> data [4][a:6]
'adhif'
>>> ##because the fourth index of the data is name, and the second to the sixth row is adhif
>>> data[0] = 'ok';data
['ok', 55, 1.57, 137, 'nadhifah chairunnisa']
>>> ##because data [0] = 'ok'; data, shows the first index to the fifth index and previously says the word ok
>>> data[-a]
'nadhifah chairunnisa'
>>> ##because data [a] shows the second index, and data [-a] shows the fifth index
>>> range (a)
range(0, 1)
>>> ##because the range starts with 0 and the value of a is 1
