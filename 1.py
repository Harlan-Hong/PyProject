##########
"""
class Test(object):

	def __init__(self, *arg):
		self.arg = arg
	
	def funA(self):
		print "a"

	@funA
	def funB(self):
		print "b"

def test(func):  
    func()  
    print "call test"  
   
def test1(f):  
    f()  
    print "call test1"  
       
def main():  
    @test  
    def fun():  
        print "call fun"  
        @test1  
        def fun1():  
            print "call fun1"  
main()  
"""
class UpperAttrMetaClass(type):
    def __new__(mcs, class_name, class_parents, class_attr):
    	print "mcs: "+ mcs  + "\nclass_name: "+ class_name +"\nclass_parents:"+ class_parents +"class_attr:" + class_attr
        attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaClass, mcs).__new__(mcs, class_name, class_parents, uppercase_attrs)


class Trick(object):
    __metaclass__ = UpperAttrMetaClass
    bar = 12
    money = 'unlimited'

print Trick.BAR
print Trick.MONEY

