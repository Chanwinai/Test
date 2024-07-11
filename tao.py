Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao1 = {'Color':'Green','Distance':100}
>>> tao.color(tao1['Color'])
>>> def rect(tao_object,tdict):
...     for i in range (4) :
...         tao_object.forward(tdict['Distance'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'Color':'Blue','Distance':60}
>>> tao2.color(tao2dict['color'])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tao2.color(tao2dict['color'])
KeyError: 'color'
