PYthon Interpreter OCT 4
(c) Microsoft Corporation. All rights reserved.

C:\Users\alfio>python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def makeCook():
...     applianceSkills={}
...     applianceSkills["riceCooker"]= 1
...     applianceSkills["microwave"] = 3
...     applianceSkills["dessert"]   = 5
...
...     aCook={}# to be changed later
...     #gordon=getACook("Ramsay")# gets gordon object
...     aCook["firstName"] ="aCook"# returns "gordon"
...     aCook["lastName"]  ="aCook"# returns "Ramsay"
...     aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
...     aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
...     aCook["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
...     #pprint.pp(aCook)
...     return aCook
... makeCook()
  File "<stdin>", line 16
    makeCook()
    ^
SyntaxError: invalid syntax
>>> makeCook()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'makeCook' is not defined
>>> def makeCook():
...     applianceSkills={}
...     applianceSkills["riceCooker"]= 1
...     applianceSkills["microwave"] = 3
...     applianceSkills["dessert"]   = 5
...
...     aCook={}# to be changed later
...     #gordon=getACook("Ramsay")# gets gordon object
...     aCook["firstName"] ="aCook"# returns "gordon"
...     aCook["lastName"]  ="aCook"# returns "Ramsay"
...     aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
...     aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
...     aCook["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
...     #pprint.pp(aCook)
...     return aCook
...
>>> def makeCook():
...     applianceSkills={}
...     applianceSkills["riceCooker"]= 1
...     applianceSkills["microwave"] = 3
...     applianceSkills["dessert"]   = 5
...
...     aCook={}# to be changed later
...     #gordon=getACook("Ramsay")# gets gordon object
...     aCook["firstName"] ="aCook"# returns "gordon"
...     aCook["lastName"]  ="aCook"# returns "Ramsay"
...     aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
...     aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
...     aCook["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
...     #pprint.pp(aCook)
... makeCook()
  File "<stdin>", line 15
    makeCook()
    ^
SyntaxError: invalid syntax
>>> def makeCook():
...     applianceSkills={}
...     applianceSkills["riceCooker"]= 1
...     applianceSkills["microwave"] = 3
...     applianceSkills["dessert"]   = 5
...
...     aCook={}# to be changed later
...     #gordon=getACook("Ramsay")# gets gordon object
...     aCook["firstName"] ="aCook"# returns "gordon"
...     aCook["lastName"]  ="aCook"# returns "Ramsay"
...     aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
...     aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
...     aCook["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
...     #pprint.pp(aCook)
...     return aCook
...
>>>
>>> makeCook()
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 6}
>>> makeCook["pizzazz"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not subscriptable
>>> makeCook()["pizzazz"]
6
>>> def setPizzazz(aCook,num):
...     aCook["pizzazz"]=num
...     return
...
>>> makeCook()["pizzazz"]
6
>>> makeCook()["setPizzazz"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'setPizzazz'
>>> x=makeCook()
>>> y=setPizazz
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setPizazz' is not defined
>>> y=setPizazz()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setPizazz' is not defined
>>> y=setPizzazz()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: setPizzazz() missing 2 required positional arguments: 'aCook' and 'num'
>>> y=setPizzazz(aCook,num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aCook' is not defined
>>> y=setPizzazz(x,num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined
>>> num=1
>>> y=setPizzazz(x,num)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 1}
>>> num = 7
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 1}
>>> num = 7
>>>
>>>
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 1}
>>> setPizzazz[x]num = 7
  File "<stdin>", line 1
    setPizzazz[x]num = 7
                 ^
SyntaxError: invalid syntax
>>> setPizzazz[num]x = 7
  File "<stdin>", line 1
    setPizzazz[num]x = 7
                   ^
SyntaxError: invalid syntax
>>> setPizzazz[x]num = 7
  File "<stdin>", line 1
    setPizzazz[x]num = 7
                 ^
SyntaxError: invalid syntax
>>> import pprint
>>> pprint.pp aCook
  File "<stdin>", line 1
    pprint.pp aCook
              ^
SyntaxError: invalid syntax
>>> pprint.pp makeCook
  File "<stdin>", line 1
    pprint.pp makeCook
              ^
SyntaxError: invalid syntax
>>> pprint.pp( makeCook)
<function makeCook at 0x00000263305DFEE0>
>>> pprint.pp( makeCook())
{'firstName': 'aCook',
 'lastName': 'aCook',
 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'],
 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5},
 'pizzazz': 6}
>>> setPizzazz([x]num) = 7
  File "<stdin>", line 1
    setPizzazz([x]num) = 7
                  ^
SyntaxError: invalid syntax
>>> setPizzazz(x,num) = 7
  File "<stdin>", line 1
    setPizzazz(x,num) = 7
    ^
SyntaxError: cannot assign to function call
>>> makeCook["pizzazz"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not subscriptable
>>> makeCook()["pizzazz"]
6
>>> pprint.pp x
  File "<stdin>", line 1
    pprint.pp x
              ^
SyntaxError: invalid syntax
>>> pprint.pp (x)
{'firstName': 'aCook',
 'lastName': 'aCook',
 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'],
 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5},
 'pizzazz': 1}
>>> pprint.pp (makeCook)
<function makeCook at 0x00000263305DFEE0>
>>> pprint.pp (makeCook())
{'firstName': 'aCook',
 'lastName': 'aCook',
 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'],
 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5},
 'pizzazz': 6}
>>> x["pizzazz"]=7
>>> x=makeCook
>>> x=makeCook()
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 6}
>>> setPizzazz(x,num)
>>>
>>>
>>>
>>>
>>> setPizzazz(x,num) = 7
  File "<stdin>", line 1
    setPizzazz(x,num) = 7
    ^
SyntaxError: cannot assign to function call
>>> setPizzazz(x,num)
>>> print(setPizzazz(x,num))
None
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 7}
>>> setPizzazz(x,num) = 15
  File "<stdin>", line 1
    setPizzazz(x,num) = 15
    ^
SyntaxError: cannot assign to function call
>>> setPizzazz(x,num) =15
  File "<stdin>", line 1
    setPizzazz(x,num) =15
    ^
SyntaxError: cannot assign to function call
>>> setPizzazz(x,num)
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 7}
>>> setPizzazz(x,num)
>>> setPizzazz(x,num) =15
  File "<stdin>", line 1
    setPizzazz(x,num) =15
    ^
SyntaxError: cannot assign to function call
>>> num
7
>>> num=15
>>> setPizzazz(x,num)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 15}
>>> setPizzazz(x)=15
  File "<stdin>", line 1
    setPizzazz(x)=15
    ^
SyntaxError: cannot assign to function call
>>> setPizzazz(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: setPizzazz() missing 1 required positional argument: 'num'
>>> setPizzazz(x,16)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 16}
>>> setPizzazz(x,3)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 3}
>>> y=joe
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'joe' is not defined
>>> y="joe"
>>> setPizzazz(y,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in setPizzazz
TypeError: 'str' object does not support item assignment
>>> setPizzazz(x,3)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 3}
>>> x[firstname]=y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'firstname' is not defined
>>> x["firstname"]=y
>>> y
'joe'
>>> type(joe)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'joe' is not defined
>>> type (y)
<class 'str'>
>>> type (x)
<class 'dict'>
>>> x=y
>>> x=4
>>> makeCook=x
>>> def makeCook():
...     applianceSkills={}
...     applianceSkills["riceCooker"]= 1
...     applianceSkills["microwave"] = 3
...     applianceSkills["dessert"]   = 5
...
...     aCook={}# to be changed later
...     #gordon=getACook("Ramsay")# gets gordon object
...     aCook["firstName"] ="aCook"# returns "gordon"
...     aCook["lastName"]  ="aCook"# returns "Ramsay"
...     aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
...     aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
...     aCook["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
...     #pprint.pp(aCook)
...     return aCook
...
>>> makeCook()=x
  File "<stdin>", line 1
    makeCook()=x
    ^
SyntaxError: cannot assign to function call
>>> x=makeCook()
>>> setPizzazz(x,35)
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 35}
>>> x=y
>>> x
'joe'
>>> x=makeCook()
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 6}
>>> y
'joe'
>>> y=MakeCook()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'MakeCook' is not defined
>>> y=makeCook()
>>> setPizzazz(y,13)
>>> y
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 13}
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 6}
>>> x="fred"
>>> x
'fred'
>>> x=makeCook()
>>> setPizzazz(x,3)
>>> "fred"=makeCook()
  File "<stdin>", line 1
    "fred"=makeCook()
    ^
SyntaxError: cannot assign to literal
>>> q="fred"
>>> q=makeCook()
>>> setPizzazz(q,-0)
>>> q
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 0}
>>> "fred"
'fred'
>>> "x"=makeCook()
  File "<stdin>", line 1
    "x"=makeCook()
    ^
SyntaxError: cannot assign to literal
>>> fred=makeCook()
>>> fred
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 6}
>>> setPizzazz(fred,-0)
>>> fred
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 0}
>>> setFistName(fred,Goober)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setFistName' is not defined
>>> setFirstName(fred,Goober)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setFirstName' is not defined
>>> setFirstName(fred,Goober)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setFirstName' is not defined
>>> def setFirstName(aCook,aName):
...     aCook["firstName"] = aName
...     return
... setFirstName(fred,Goober)
  File "<stdin>", line 4
    setFirstName(fred,Goober)
    ^
SyntaxError: invalid syntax
>>> def setFirstName(aCook,aName):
...     aCook["firstName"] = aName
...     return
...
...
>>> def setFirstName(aCook,aName):
...     aCook["firstName"] = aName
...     return
...
>>> def setFirstName(aCook,aName):
...     aCook["firstName"] = aName
...     return
...
>>>
>>> setFirstName(fred,goober)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'goober' is not defined
>>> setFirstName(fred,"goober")
>>> fred
{'firstName': 'goober', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 0}
>>> def setSkillLevel(cook,appliance,num):
...     cook["skillLevel"][appliance]=num
...     return
...
>>>
>>> setSkillLevel(goober,dessert,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'goober' is not defined
>>> setSkillLevel("goober",dessert,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dessert' is not defined
>>> setSkillLevel("goober","dessert",6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in setSkillLevel
TypeError: string indices must be integers
>>> setSkillLevel(cook,"dessert",7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cook' is not defined
>>> goober
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'goober' is not defined
>>> type(goober)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'goober' is not defined
>>> type("goober")
<class 'str'>
>>> type(fred)
<class 'dict'>
>>> goober=makeCook()
>>> setSkillLevel(goober,"dessert",7)
>>>
>>>
>>> x
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5}, 'pizzazz': 3}
>>> goober
{'firstName': 'aCook', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 7}, 'pizzazz': 6}
>>> setSkillLevel(goober,"dessert",7)
>>> setSkillLevel(fred,"microwave",80)
>>> fred
{'firstName': 'goober', 'lastName': 'aCook', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 80, 'dessert': 5}, 'pizzazz': 0}
>>> def setLastName(aCook,lName):
...     aCook["lastName"] = lName
...     return
...
>>>
>>> setLastName(fred,"Goober")
>>>
>>> fred
{'firstName': 'goober', 'lastName': 'Goober', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 80, 'dessert': 5}, 'pizzazz': 0}
>>> sally=makeCook()
>>> setFirstName(sally,"sally")
>>> setLastName(sally,"stanley")
>>> setPizzazz(sally,999)
>>> setSkillLevel(sally,"ricecooker"-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> setSkillLevel(sally,"ricecooker",-1)
>>> sally
{'firstName': 'sally', 'lastName': 'stanley', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5, 'ricecooker': -1}, 'pizzazz': 999}
>>> setSkillLevel(sally,"riceCooker",-1)
>>> sally
{'firstName': 'sally', 'lastName': 'stanley', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': -1, 'microwave': 3, 'dessert': 5, 'ricecooker': -1}, 'pizzazz': 999}
>>> setSkillLevel(sally,"microwave",10)
>>> setSkillLevel(sally,"dessert",10)
>>> sally
{'firstName': 'sally', 'lastName': 'stanley', 'appliances': ['::ricecooker::', '::microwave::', '::dessert::'], 'skillLevel': {'riceCooker': -1, 'microwave': 10, 'dessert': 10, 'ricecooker': -1}, 'pizzazz': 999}
>>> def setLastName(aCook,lName):
...     aCook["lastName"] = lName
...     returndef setLastName(aCook,lName):
  File "<stdin>", line 3
    returndef setLastName(aCook,lName):
              ^
SyntaxError: invalid syntax
>>>     aCook["lastName"] = lName
  File "<stdin>", line 1
    aCook["lastName"] = lName
IndentationError: unexpected indent
>>>     return
