'''def my_function():
  print("Malli")
my_function()'''

'''def my_function(fname,lname):
    print(fname + "hello" +lname)
my_function("hi","hy")
my_function("welcome","malli")'''



'''def malli(*name):
    print("My name is" +name[0])
malli("malli","malleswari")'''



'''def helo(**name):
    print("Hi Welcome"+ name["fname"])
helo(fname = "sir",lname="mam")'''


#default parameter value
'''def fun(village="kng"):
    print("my vlg name is"  +village)
fun("koti")
fun("ong")
fun()'''

'''def fun(a,b):
    print(a,b)
fun(2,3)'''

'''def fun(a,b):
    return a+b
a=fun(2,3)
print(a)'''

'''def fun(a):
    return a*3
print(fun(3))'''


'''def fun(a):
    for i in a:
        print(i)
fun([1,2,3,4,5])'''

def fun(*a):
    print(a)
fun(1,6,7,8,9)

def hi(**b):
    print(b)
hi(name='malli',age=20)




