import random 

print(random.random())

print(random.randrange(1,7,2))

print(random.randint(1,10))


a=["hi","hello","welcome"]
print(random.choice(a))


i=['A','B','C']
random.shuffle(i)
print(i)

c=[2,5,3,1]
random.shuffle(c)
print(c)

print(random.sample([1,2,3,4,5],2))
print(random.sample((10,20,30),1))

print(random.choices(('a','d','g','h'),k=2))

print(random.uniform(67,89))


print(random.randint(2,10))
print(random.seed((4)))
print(random.randint(2,10))


