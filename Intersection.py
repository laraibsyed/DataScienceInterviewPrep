def intersection(x, y):
   return list(set(x) & set(y))

x= [1,5,9,0]
y = [3,0,2,9]
result = intersection(x,y)

print(result)

# set(x) and set(y) converts the arrays into sets
# & is the intersection operator for sets
# list() converts them back to arrays