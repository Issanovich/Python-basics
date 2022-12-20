Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Hash Table
>>> #creating dictionaries
>>> 
>>> my_dict={'Jeremy':'001','Issah':'002':'Benny':'003'}
SyntaxError: invalid syntax
>>>  my_dict={'Jeremy':'001','Issah':'002','Benny':'003'}
 
SyntaxError: unexpected indent
>>> my_dict={'Jeremy':'001','Issah':'002','Benny':'003'}
>>> print(my_dict)
{'Jeremy': '001', 'Issah': '002', 'Benny': '003'}
>>> type(my_dict)
<class 'dict'>
>>> 
>>> new_dict=dict()
>>> print(new_dict)
{}
>>> type(new_dict)
<class 'dict'>
>>> 
>>> new_dict=dict{'Jeremy':'001','Issah':'002':'Benny':'003'}
SyntaxError: invalid syntax
>>> new_dict=dict('Jeremy':'001','Issah':'002':'Benny':'003')
SyntaxError: invalid syntax
>>> new_dict=dict('Jeremy'='001','Issah'='002':'Benny'='003')
SyntaxError: invalid syntax
>>> new_dict=dict('Jeremy'='001','Issah'='002','Benny'='003')
SyntaxError: keyword can't be an expression
>>> new_dict=dict{'Jeremy'='001','Issah'='002','Benny'='003'}
SyntaxError: invalid syntax
>>> new_dict=dict('Jeremy'='001','Issah'='002','Benny'='003')
SyntaxError: keyword can't be an expression
>>> 
>>> #Nested Dictionary
>>> emp_details={'employee':{'Jeremy':{'ID':'001','Salary':'5000', 'Designation','team lead'},'Richy':{'ID':'002','Salary':'2000','Designation','Associate'}}}
SyntaxError: invalid syntax
>>> 
>>> emp_details={'employee':{'Jeremy':{'ID':'001','Salary':'5000', 'Designation':'team lead'},'Richy':{'ID':'002','Salary':'2000','Designation':'Associate'}}}
>>> print(emp_details)
{'employee': {'Jeremy': {'ID': '001', 'Salary': '5000', 'Designation': 'team lead'}, 'Richy': {'ID': '002', 'Salary': '2000', 'Designation': 'Associate'}}}
>>> 
>>> #Accessing Items
>>> my_dict['jeremy']
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    my_dict['jeremy']
KeyError: 'jeremy'
>>> my_dict['Jeremy']
'001'
>>> print(my_dict)
{'Jeremy': '001', 'Issah': '002', 'Benny': '003'}
>>> print(my_dict.keys())
dict_keys(['Jeremy', 'Issah', 'Benny'])
>>> print(my_dict.values())
dict_values(['001', '002', '003'])
>>> print(emp_details)
{'employee': {'Jeremy': {'ID': '001', 'Salary': '5000', 'Designation': 'team lead'}, 'Richy': {'ID': '002', 'Salary': '2000', 'Designation': 'Associate'}}}
>>> print(emp_details.keys())
dict_keys(['employee'])
>>> print(emp_details.values())
dict_values([{'Jeremy': {'ID': '001', 'Salary': '5000', 'Designation': 'team lead'}, 'Richy': {'ID': '002', 'Salary': '2000', 'Designation': 'Associate'}}])
>>> print(emp_details.get(Richy))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(emp_details.get(Richy))
NameError: name 'Richy' is not defined
>>> print(my_dict.get(Benny))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(my_dict.get(Benny))
NameError: name 'Benny' is not defined
>>> print(emp_details.get('Richy'))
None
>>> print(my_dict.get('Benny'))
003
>>> for x in my_dict:
	print(x)

	
Jeremy
Issah
Benny
>>> 
>>> for x in emp_details:
	print (x)

	
employee
>>> 
>>> for x in my_dict.values:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    for x in my_dict.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for x in my_dict.values():
	print(x)

	
001
002
003
>>> 
>>> for x,y in my_dict.items():
	print(x,y)

	
Jeremy 001
Issah 002
Benny 003
>>> 
>>> #Updating data in dictionary
>>> 
>>> my_dict['Jeremy']='004'
>>> my_dict['Kwame']='002'
>>> print(my_dict)
{'Jeremy': '004', 'Issah': '002', 'Benny': '003', 'Kwame': '002'}
>>> 
>>> #Deletiing
>>> 
>>> my_dict.pop('Kwame')
'002'
>>> 
>>> my_dict.popitem()
('Benny', '003')
>>> print(my_dict)
{'Jeremy': '004', 'Issah': '002'}
>>> del my_dict['Jeremy']
>>> print (my_dict)
{'Issah': '002'}
>>> 
>>> #Dict to df
>>> 
>>> import pandas as pd
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
>>> import pandas
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
>>> 
