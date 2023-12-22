d={1:50,2:20}
print(d[2])

#get
dict={1:'hi',2:'hello'}
print(dict.get(1))

print(dict.keys())

print(dict.values())

print(dict.items())

dict.update({3:'malli'})
print(dict)

for i,j in {1:'hi',2:'hello'}.items():
  print(i,j)
