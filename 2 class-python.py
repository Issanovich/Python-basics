Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##ARRAY ARRAY ARRAY
>>> 
>>> import array
>>> a=array.array('1',[1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=array.array('1',[1,2,3,4,5,6])
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
>>> a=array.array('int',[1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=array.array('int',[1,2,3,4,5,6])
TypeError: array() argument 1 must be a unicode character, not str
>>> a=array.array('i',[1,1,2,3,4,5,6])
>>> print(a)
array('i', [1, 1, 2, 3, 4, 5, 6])
>>> import array as arr
>>> a=arr.array('1',[1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=arr.array('1',[1,2,3,4,5,6])
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
>>> a=arr.array('i',[1,2,3,4,5,6])
>>> print(a)
array('i', [1, 2, 3, 4, 5, 6])
>>> 
>>> from array import*
>>> a=array('i',[1,2,3,4,5])
>>> print (a)
array('i', [1, 2, 3, 4, 5])
>>> 
>>> #Accessing Array Elements
>>> a[2]
3
>>> print(a[2])
3
>>> 
>>> #Lenght of an array
>>> print (len(a))
5
>>> 
>>> #Adding Elements to an Array
>>> # append()	extend()	insert()
>>> print(a)
array('i', [1, 2, 3, 4, 5])
>>> 
>>> a.append(8)
>>> print(a)
array('i', [1, 2, 3, 4, 5, 8])
>>> 
>>> a.extend[2,4,65]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.extend[2,4,65]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.extend([2,4,65])
>>> print(a)
array('i', [1, 2, 3, 4, 5, 8, 2, 4, 65])
>>> 
>>> a.insert(3,100)
>>> print (a)
array('i', [1, 2, 3, 100, 4, 5, 8, 2, 4, 65])
>>> a.insert(1,9,2,99)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.insert(1,9,2,99)
TypeError: insert() takes exactly 2 arguments (4 given)
>>> 
>>> #RemovingElementsOfAnArray
>>> 
>>> #RemovingElementsOfAnArray
>>> #	pop()	remove()
>>> #	pop(index)	remove(number)
>>> print(a)
array('i', [1, 2, 3, 100, 4, 5, 8, 2, 4, 65])
>>> a.pop
<built-in method pop of array.array object at 0x0000000002C49070>
>>> a.pop()
65
>>> print(a)
array('i', [1, 2, 3, 100, 4, 5, 8, 2, 4])
>>> a.pop(3)
100
>>> print(a)
array('i', [1, 2, 3, 4, 5, 8, 2, 4])
>>> a.pop(-2)
2
>>> print(a)
array('i', [1, 2, 3, 4, 5, 8, 4])
>>> a.remove(4)
>>> print(a)
array('i', [1, 2, 3, 5, 8, 4])
>>> 
>>> #Array Concatenation (joining of arrays)
>>> b=array.array('i',[1,3,5,6,7,88])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b=array.array('i',[1,3,5,6,7,88])
AttributeError: type object 'array.array' has no attribute 'array'
>>> import arrar
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    import arrar
ModuleNotFoundError: No module named 'arrar'
>>> import array
>>> d=array.array('i',[2,3,4,5,6,7])
>>> c=array.array('i',[3,6,7,9])
>>> d=array.array('i')
>>> 
>>> b=array.array('i',[2,3,4,5,6,7])
>>> c=array.array('i',[3,6,7,9])
SyntaxError: multiple statements found while compiling a single statement
>>> b=array.array('i',[2,3,4,5,6,7])
>>> c=array.array('i',[3,6,7,9])
>>> e=array.array('i')
>>> e=b+c
>>> print(e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>>> 
>>> #SLICING Arrays
>>> print(e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>>> e[0:6]
array('i', [2, 3, 4, 5, 6, 7])
>>> e[0:-3]
array('i', [2, 3, 4, 5, 6, 7, 3])
>>> e[::-1]
array('i', [9, 7, 6, 3, 7, 6, 5, 4, 3, 2])
>>> print(e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>>> 
>>> #LOOPING THROUGHT ARRAYS
>>> print(e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>>> 
>>> for x in e
SyntaxError: invalid syntax
>>> for x in e;
SyntaxError: invalid syntax
>>> for x in e :
	print(x)

	
2
3
4
5
6
7
3
6
7
9
>>> 
>>> for x in e[0:-2] :
	print(x)

	
2
3
4
5
6
7
3
6
>>> 
>>> print(e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>>> 
>>> jerey=0
>>> while jerey < e[3]:
	print(e[jerey])
	jerey=jerey+1

	
2
3
4
5
6
>>> 
>>> print (e)
array('i', [2, 3, 4, 5, 6, 7, 3, 6, 7, 9])
>> 
 






	
