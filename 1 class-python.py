Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #multiply two variables
>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> #multiply two variables
>>> a=2
>>> b=3
>>> c=a*b
>>> print(c)
6
>>> #Add two variables
>>> a=40
>>> f=89
>>> g=a+f
>>> print(g)
129
>>> #comments in python
>>> #multi-line comments
>>> #program to multiply 2 integers
>>> a=4
>>> b=2
>>> a*b
8
>>> comments in python
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    comments in python
NameError: name 'comments' is not defined
>>> '''
docstrings are not omitted by the intepreter
'''
'\ndocstrings are not omitted by the intepreter\n'
>>> '''
docstrings are not omitted by the intepreter
'''
'\ndocstrings are not omitted by the intepreter\n'
>>> '''
placing it before the code
''' a=1
SyntaxError: invalid syntax
>>> q=3
>>> d=4
>>> a+d
8
>>> s
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 10
>>> r = 12
>>> s*r
120
>>> s/r
0.8333333333333334
>>> s%r
10
>>> s-r
-2
>>> r-s
2
>>> x = 23
>>> type(x)
<class 'int'>
>>> s=21.44
>>> type(s)
<class 'float'>
>>> f=23j
>>> type(f)
<class 'complex'>
>>> num = 10 > 9
>>> type(num)
<class 'bool'>
>>> print(num)
True
>>> name = 'eedurika'
>>> len (name)
8
>>> name(2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name(2)
TypeError: 'str' object is not callable
>>> num (2)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    num (2)
TypeError: 'bool' object is not callable
>>> name(2)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    name(2)
TypeError: 'str' object is not callable
>>> name = 'edurika'
>>> len (name)
7
>>> name[2]
'u'
>>> name[2:8]
'urika'
>>> name.upper()
'EDURIKA'
>>> name.lower()
'edurika'
>>> name[-1]
'a'
>>> x= 'hello'
>>> y= 'world'
>>> print(x*y)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(x*y)
TypeError: can't multiply sequence by non-int of type 'str'
>>> z=x*y
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    z=x*y
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('x*y')
x*y
>>> x*y
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'str'
>>> mylist = [10,20,34,10, 'jeremy', 'issah-mcanderson']
>>> print(mylist)
[10, 20, 34, 10, 'jeremy', 'issah-mcanderson']
>>> mylist[2:4]
[34, 10]
>>> mylist[2]=40
>>> print(mylist)
[10, 20, 40, 10, 'jeremy', 'issah-mcanderson']
>>> mylist.reverse()
>>> print(mylist)
['issah-mcanderson', 'jeremy', 10, 40, 20, 10]
>>> siblings={1:'Ibrahim',
	  2:'Ps Brian Issac',
	  'third':'Moro Issah'}
>>> print(siblings)
{1: 'Ibrahim', 2: 'Ps Brian Issac', 'third': 'Moro Issah'}
>>> siblings['third']
'Moro Issah'
>>> siblings.get('third')
'Moro Issah'
>>> siblings['third']= Benny
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    siblings['third']= Benny
NameError: name 'Benny' is not defined
>>> siblings['third']='Benny'
>>> print(siblngs)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(siblngs)
NameError: name 'siblngs' is not defined
>>> print(siblings)
{1: 'Ibrahim', 2: 'Ps Brian Issac', 'third': 'Benny'}
>>> siblings.reverse()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    siblings.reverse()
AttributeError: 'dict' object has no attribute 'reverse'
>>> 
>>> print (siblings)
{1: 'Ibrahim', 2: 'Ps Brian Issac', 'third': 'Benny'}
>>> siblings['fourth']='Jeremy Kwame Issah'
>>> print(siblings)
{1: 'Ibrahim', 2: 'Ps Brian Issac', 'third': 'Benny', 'fourth': 'Jeremy Kwame Issah'}
>>> print(siblings)
{1: 'Ibrahim', 2: 'Ps Brian Issac', 'third': 'Benny', 'fourth': 'Jeremy Kwame Issah'}
>>> #TUPLE TUPLE TURPLE TURPLE
>>> animals = (10,12,43, 'monkey', 'rat', 'mouse')
>>> animals[4]
'rat'
>>> animals.count('mouse')
1
>>> ###SET SET SET SET
>>> myset={23,435,32,32,54, 'benz','toyota')
SyntaxError: invalid syntax
>>> myset={23,43,43,56,'BMW','TOYOTA'}
>>> print(myset)
{'BMW', 43, 'TOYOTA', 23, 56}
>>> myset={12,212,21,12,'mum','dad'}
>>> print(myset)
{'mum', 'dad', 12, 212, 21}
>>> range(10)
range(0, 10)
>>> list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range.odd(20)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    range.odd(20)
AttributeError: type object 'range' has no attribute 'odd'
>>> a=[1,2,3,4,5,6]
>>> b=[3,3,2,5,6]
>>> d=[a,b]
>>> print(d)
[[1, 2, 3, 4, 5, 6], [3, 3, 2, 5, 6]]
>>> ###TYPE CONVERSION
>>> X=3
>>> T= 'ME'
>>> print(X*T)
MEMEME
>>> print(X+T)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print(X+T)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(X)+T)
3ME
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> int(X)
3
>>> str(x)
'hello'
>>> print (str(x)+str(y))
helloworld
>>> print (str(x) + str(y) )
helloworld
>>> print(x+y)
helloworld
>>> print(str(x)*str(y))
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    print(str(x)*str(y))
TypeError: can't multiply sequence by non-int of type 'str'
>>> ##PYTHON COLLECTIONS
>>> # Lists()	Turples()		Sets	Dictionary dic()
>>> #List[]
>>> from collections import namedtuple
>>> a=namedtuple('courses','name','technology')
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a=namedtuple('courses','name','technology')
TypeError: namedtuple() takes 2 positional arguments but 3 were given
>>> a = namedtuple('courses', 'name', technology')
	       
SyntaxError: EOL while scanning string literal
>>> a = namedtuple('courses', 'name', 'technology')
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a = namedtuple('courses', 'name', 'technology')
TypeError: namedtuple() takes 2 positional arguments but 3 were given
>>> a = namedtuple('courses', 'name, technology')
>>> s=('data science', 'python')
>>> print(s)
('data science', 'python')
>>> 
>>> #namedtuple uses on two variables
>>> a = namedtuple('courses', 'name, technology')
>>> s=a('data science', 'python')
>>> print(s)
courses(name='data science', technology='python')
>>> s=a.make(['artificial intelligence','python'])
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    s=a.make(['artificial intelligence','python'])
AttributeError: type object 'courses' has no attribute 'make'
>>> a=namedtuple('courses', 'name, technology')
>>> s=a.make(['artificial intelligence','python'])
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    s=a.make(['artificial intelligence','python'])
AttributeError: type object 'courses' has no attribute 'make'
>>> #Deque
>>> #makes deleting easy
>>> from collection import deque
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    from collection import deque
ModuleNotFoundError: No module named 'collection'
>>> from collections import deque
>>> a=['j', 'e','r','e','m','y']
>>> d=deque(y)
>>> print(d)
deque(['w', 'o', 'r', 'l', 'd'])
>>> d=deque (a)
>>> print(a)
['j', 'e', 'r', 'e', 'm', 'y']
>>> d.append('isshnovich')
>>> print(d)
deque(['j', 'e', 'r', 'e', 'm', 'y', 'isshnovich'])
>>> deque(['j', 'e', 'r', 'e', 'm', 'y', 'isshnovich'])
deque(['j', 'e', 'r', 'e', 'm', 'y', 'isshnovich'])
>>> d.appendleft('issahnovich')
>>> print(d)
deque(['issahnovich', 'j', 'e', 'r', 'e', 'm', 'y', 'isshnovich'])
>>> d.pop()
'isshnovich'
>>> print (d)
deque(['issahnovich', 'j', 'e', 'r', 'e', 'm', 'y'])
>>> d.popleft()
'issahnovich'
>>> print(d)
deque(['j', 'e', 'r', 'e', 'm', 'y'])
>>> ##CHAINMAP CHAINMAP
>>> from collections import chainmap
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    from collections import chainmap
ImportError: cannot import name 'chainmap' from 'collections' (C:\Users\User\AppData\Local\Programs\Python\Python37\lib\collections\__init__.py)
>>> from collections import ChainMap
>>> a={1:'edurika', 2:'python'}
>>> b={3:'Machine learning', 4:'Artificail Inteligence'}
>>> a1=ChainMap(a,b)
>>> print(a1)
ChainMap({1: 'edurika', 2: 'python'}, {3: 'Machine learning', 4: 'Artificail Inteligence'})
>>> 
>>> #COUNTER COUNTER
>>> from collections import Counter
>>> a=[1,1,1,,3,4,6,6,7,9,4,9,9]
SyntaxError: invalid syntax
>>> a=[1,1,1,2,4,56,6,5,9,8,2,0]
>>> c=Counter(a)
>>> print(c)
Counter({1: 3, 2: 2, 4: 1, 56: 1, 6: 1, 5: 1, 9: 1, 8: 1, 0: 1})
>>> print(list(c.elements()))
[1, 1, 1, 2, 2, 4, 56, 6, 5, 9, 8, 0]
>>> print(c.most_common())
[(1, 3), (2, 2), (4, 1), (56, 1), (6, 1), (5, 1), (9, 1), (8, 1), (0, 1)]
>>> sub={2:1,6:1}
>>> print(c.subtract(sub))
None
>>> 
>>> ##OrderedDict
>>> from collections import OrderedDict
>>> d= OrderedDict()
>>> d[1]='j'
>>> d[2]='e'
>>> d[3]='r'
>>> d[4]='e'
>>> d[5]='m'
>>> d[6]='y'
>>> print(d)
OrderedDict([(1, 'j'), (2, 'e'), (3, 'r'), (4, 'e'), (5, 'm'), (6, 'y')])
>>> print(d.keys())
odict_keys([1, 2, 3, 4, 5, 6])
>>> print(d.items())
odict_items([(1, 'j'), (2, 'e'), (3, 'r'), (4, 'e'), (5, 'm'), (6, 'y')])
>>> d[6]='ie'
>>> print(d)
OrderedDict([(1, 'j'), (2, 'e'), (3, 'r'), (4, 'e'), (5, 'm'), (6, 'ie')])
>>> 
>>> ###defaultdict
>>> d=default(int)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    d=default(int)
NameError: name 'default' is not defined
>>> d=defaultdict(int)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    d=defaultdict(int)
NameError: name 'defaultdict' is not defined
>>> from collections import defaultdict
>>> d=defaultdict(int)
>>> d[1]='Jeremy'
>>> d[2]='Issah-McAnderson'
>>> print(d)
defaultdict(<class 'int'>, {1: 'Jeremy', 2: 'Issah-McAnderson'})
>>> print(d[3])
0
>>> 
