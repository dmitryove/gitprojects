print "========================= Property ====================="
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 100
print c.x

print "======================= DESCRIPTOR ================================"

class A(object):
    def __init__(self, val):
        self.val = val

    def __set__(self, instance, value):
        self.val = value

    def __get__(self, instance, owner):
        return self.val

class B(object):
    a1 = A(10)
    a2 = A(20)

b = B()
b1 = B()
b.a1 = 10
b.a2 = 20
b1.a1 = 30
b1.a2 = 40

print "b.a1 %d" % b.a1
print "b.a2 %d" % b.a2

print "b1.a1 %d" % b1.a1
print "b1.a2 %d" % b1.a2


#fuction as a decorator
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello habr"

print hello()


# Class as a decorator
print "============= Class as a descriptor ==============="
class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

func1()
func2()

print "================ Inheritance: attrbute from the class ================="
class Base():
    var = 1

class Kid1(Base):
    var2 = 2

class Kid2(Base):
    var3 = 3

kid1 = Kid1()
kid2 = Kid2()
kid1.var = 20
Base.var = 10


print kid1.var
print kid2.var

print "========= Generator =================="
class Bank(): # let's create a bank, building ATMs
    crisis = False
    def create_atm(self):
        print "entering generator"
        while not self.crisis:
            print "before yield"
            yield "$100"
            print "after yield"

hsbc = Bank() # when everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm()

print(corner_street_atm.next())
print(corner_street_atm.next())

hsbc.crisis = True # crisis is coming, no more money!
try:
    print(corner_street_atm.next())
except StopIteration:
    print "Generator ends"

