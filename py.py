# learn how does its work...
import math

class myC:
	def __init__(self, counter=0, attr=0):
		self.counter = counter
		self.attr = attr

	def setAttr(self, f_attr):
		self.counter = self.counter +1
		self.attr = f_attr
	def getAttr(self):
		self.counter = self.counter +1
		return self.attr
	def countAttr(self):
		self.counter = self.counter +1
		return self.counter


# code

myc1 = myC(1,0);

print "f_counter is", myc1.countAttr()
print "and again?: ", myc1.countAttr()

print "f(x) is myC"
print "myC.attr is", myc1.attr

print "change..."
prom = int(input("New paramz?: "))
myc1.setAttr(prom)

print "myC.attr now is", myc1.attr

print "at the end of all counter is:", myc1.countAttr()
