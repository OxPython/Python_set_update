'''
Created on Jul 9, 2014

@author: viejoemer

HowTo insert items from one set to another?

¿Cómo insertar elementos de un set a otro?

update(other, ...)
set |= other | ...
Update the set, adding elements from all others.
'''

#Create a set with values.
s = set([0,1,2,3])
print("set one", s)

s2 = set([1,6])
print("set two", s2)

#Update a set with other
s.update(s2)
print("set one, updated", s)
print("set two", s2)
#Be careful because in a set there are not equal elements 

#Another way is set |= other
s3 = {0, 1, 2, 3}
s2 |= s3
print("set two, updated", s2)