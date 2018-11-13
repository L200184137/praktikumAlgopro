Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = 'nadhifah chairunnisa'
>>> NIM = 'L200184137'
>>> x = '1'+NIM[7:]
>>> a = int (x)
>>> b = len (name)
>>> type (a)
<class 'int'>
>>> ##because x which is originally a string has been converted into an integer using the variable int (). this can also be called a type cast
>>> type (b)
<class 'int'>
>>> ##because variable b represents the number of members of the variable name. and the number in integer type because it is an integer
>>> a/b
56.85
>>> ##because variable (a) is rooted with variable (b)
>>> a//b
56
>>> ##because variable (a) is raised twice with variable (b)
>>> 10*(a-199)
9380
>>> ##because in integer operations it uses rumus algebra which prioritizes the numbers in parentheses first after multiplication and then the addition and subtraction.
>>> b**2
400
>>> ##because variable (b) has a rank 2
>>> a%b
17
>>> ##because the variable (a) is divided by variable (b)
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> ##because the float indicates that the varabel is a decimal number
>>> a/c
90.96
>>> ##because variable (a) is rooted with variable (c)
>>> a//c
90.0
>>> ##because variable (a) is raised twice with variable (c)
>>> a%c
12.0
>>> ##because the variable (a) is divided by variable (c)
>>> c>b
False
>>> ##because the command that is input is wrong and and the program shows the word "false"
>>> type(c>b)
<class 'bool'>
>>> ##bool is boolean, which shows the command in the program "true" or "false"
>>> a>b and b>c
True
>>> ##because the command that is input is right and and the program shows the word "true"
>>> a>1100 or b<10
True
>>> ##because the command that is input is right and and the program shows the word "true"
