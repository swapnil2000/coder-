Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> a=datetime.datetime.today()
>>> print(a)
2020-04-22 13:08:21.327006
>>> a=datetime.timedelta()
>>> print(a)
0:00:00
>>> a=datetime.datetime.today()+datetime.timedelta(days=10)
>>> print(a)
2020-05-02 13:10:05.009087
>>> import string
>>> print(string.ascii_letters)
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
>>> print(string.ascii_uppercase)
ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> print(string.digits)
0123456789
>>> print(string.hexdigits)
0123456789abcdefABCDEF
>>> print(string.octdigits)
01234567
>>> print(string.whitespace)
 	

>>> print(string.punctuation)
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> l=[]
>>> l.append(string.punctuation)
>>> print(l)
['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
>>> l2=[]
>>> for i in l:
	l2.append(i)

	
>>> print(l2)
['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
>>> 