Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> format (12345.6789, '.2f')
'12345.68'
>>>  print(format(12345.6789, '.2f'))
 
SyntaxError: unexpected indent
>>> print(format(12345.6789, '.2f'))
12345.68
>>> print(format(12345.6789, '.1f'))
12345.7
>>> print("The number is", format(1.234567, '.2f'))
The number is 1.23
>>> print(format(12345.6789, ',.2f'))
12,345.68
>>> print(format(123456789.456, ',.2f'))
123,456,789.46
>>> print(format(12345.6789, 'f'))
12345.678900
>>> print("The number is", format(12345.6789, '10,.3f'))
The number is 12,345.679
>>> 
>>> print("The number is", format(12345.6789, '12,.3f'))
The number is   12,345.679
>>> 
>>> print("The number is", format(12345.6789, '12,.3f'))
The number is   12,345.679
>>>  print(format(123456, '10,d'))

SyntaxError: unexpected indent
>>> print(format(123456, '10,d'))
   123,456
>>> print(format(0.5, '%'))
50.000000%
>>> print(format(0.5, '.0%'))
50%
>>> print(format(0.5, '.2%))
	     
SyntaxError: EOL while scanning string literal
>>> print(format(0.5, '.2%))
	     
SyntaxError: EOL while scanning string literal
>>> print(format(0.5, '.2%'))
50.00%
>>> 
