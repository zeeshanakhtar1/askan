Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('helloworld')
helloworld
>>> a = 'ab khud kuch kerna parega'
>>> b = 'hum ko mehnat kerni paregi
SyntaxError: EOL while scanning string literal
>>> 
>>> b = 'hum ko mehnat aur lagan se kaam kerna hoga'
>>> c = a + b
>>> print (c)
ab khud kuch kerna paregahum ko mehnat aur lagan se kaam kerna hoga
>>> a1 = 'ab khud kuch kerna parega'
>>> b1 = %%'hum ko mehnat aur lagan se kaam kerna hoga'
SyntaxError: invalid syntax
>>> print (b1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print (b1)
NameError: name 'b1' is not defined
>>> b1= //'hum ko mehnat aur lagan se kaam kerna hoga'
SyntaxError: invalid syntax
>>> b1= % 'hum ko mehnat aur lagan se kaam kerna hoga'
SyntaxError: invalid syntax
>>> c = 'abey gap kaise doon?'
>>> d = "koshish karo"
>>> e = c / d
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    e = c / d
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> str = 'abey gap nai do function ka naam likha jaisa is mai str use kia hai string k liye'
>>> print str
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(str)?
>>> print (str)
abey gap nai do function ka naam likha jaisa is mai str use kia hai string k liye
>>> str ' shabash'
SyntaxError: invalid syntax
>>> str a = 'shabash samjh rahe ho'
SyntaxError: invalid syntax
>>> print ('shabash samjh rahe ho')
shabash samjh rahe ho
>>> print ('bachodi jari rakho')
bachodi jari rakho
>>> 
