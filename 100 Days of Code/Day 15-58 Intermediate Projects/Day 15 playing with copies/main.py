from TestObject import TestObject
import copy

a = TestObject("foobar")
print(a.name)
b = copy.deepcopy(a)
b.name = "test"
print(a.name)
print(b.name)
