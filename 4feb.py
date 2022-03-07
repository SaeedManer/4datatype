#datatype list
#x = ['bat', 'ball', 'stump']
#print(x)

#y = ['saeed', 25, True, 25.55, '32']
#print(y[:3])

#y = ['saeed', 25, True, 25.55, '32']
#print(y[1:3])

#r = ["red", "blue", "black", "yellow", "pink"]
#r[2] = "purple"
#print(r)


#r = ["red", "blue", "black", "yellow", "pink"]
#r[1:3] = ["purple", "grey"]
#print(r)

#x = ("saeed")
#print(x)





#add list Items
#r = ["red", "blue", "black", "yellow", "pink"]
#r.append("orange")
#print(r)


#r = ["red", "blue", "black", "yellow", "pink"]
#r.insert(2,"orange")
#print(r)

#c = ["red", "blue", "black", "yellow", "pink"]
#d = ["bat", "cat", "fat"]
#c.extend(d)
#print(c)


#r = ("red", "blue", "black", "yellow", "pink")
#r.insert(2,"orange")
#print(len(r))

#r = ("tuple",)
#print(type(r))






#Access Tuples

#r = ("red", "blue", "black", "yellow", "pink")
#r.insert(2,"orange")
#print(r[1])


#r = ("red", "blue", "black", "yellow", "pink")
#r.insert(2,"orange")
#print(r[0:2])


#r = ("red", "blue", "black", "yellow", "pink")
#r.insert(2,"orange")
#print(r[:4])

#r = ("red", "blue", "black", "yellow", "pink")
#if "red" in r:
#    print("yes")


#x = ('apple', 'banana', 'grapes')
#y = list(x)
#y[1] = 'mango'
#x = tuple(y)

#print(x)






#Update tuple

#x = ('apple', 'banana', 'grapes')
#y = list(x)
#y.append('mango')
#x = tuple(y)

#print(x)


#x = ('apple', 'banana', 'grapes')
#y = ('mango',)
#x += y

#print(x)






#Unpack Tuples
#x = ('apple', 'banana', 'grapes')
#(a,b,c) = x

#print(a)
#print(b)


#x = ('apple','cherry', 'strawberry', 'banana', 'grapes')
#(a, *b, c) = x
#print(b)
#print(c)





#Loop Tuples

#y = ("apple", "banana", "cherry")
#for x in y:
 #   print(x)


#thistuple = ("apple", "banana", "cherry")
#for x in thistuple:
#  print(x)




#Join Tuples

#x = ("apple", "banana", "cherry")
#y = (1, 2, 3)

#z = x + y
#print(z)


#x = ("apple", "banana", "cherry")
#y = x * 2
#print(y)






#SETS
#SETS

#Python set

#x = {"apple", "banana", "cherry"}
#print(x)


#x = {"apple", "banana", "cherry"}
#print(len(x))

#x = {"apple", "banana", "cherry"}
#y = {1,2,3,4}
#z = {True,False,True}

#print(type(x))
#print(type(y))
#print(type(z))


#x = set(("apple", "banana", "cherry"))
#print(x)

#x = {"apple", "banana", "cherry"}
#if "apple" in x:
#    print("yes")



#r = {"red", "blue", "black", "yellow", "pink"}
#if "red" in r:
#    print("yes")



#x = {"apple", "banana", "cherry"}
#x.add("green")
#print(x)



#x = {"apple", "banana", "cherry"}
#y = {"red", "green", "blue",}
#x.update(y)
#print(x)


#x = {"apple", "banana", "cherry"}
#x.remove("apple")
#print(x)


#x = {"apple", "banana", "cherry"}
#x.discard("apple")
#print(x)


#x = {"apple", "banana", "cherry"}
#x.clear()
#print(x)


#x = {"apple", "banana", "cherry"}
#for y in x:
#    print(y)



#x = {"apple", "banana", "cherry"}
#y = {"red", "green", "blue",}
#z = x.union(y)
#print(z)


#x = {"apple", "banana", "cherry"}
#y = {"red", "green", "blue", "apple"}
#z = x.intersection(y)
#print(z)






#Dictonary
#Dictonary

#a = {
#    "x": "red",
 #   "y": "blue",  
#    "z": "green",
 #   }
#print(a)


#a = {
#    "x": "red",
#    "y": "blue",  
 #   "z": "green",
#    }
#print(a["x"])



#a = {
#    "x": "red",
#    "y": "blue",  
#    "z": "green",
#    }
#print(len(a))



#a = {
#    "x": "red",
#    "y": "blue",  
#    "z": "green",
#    }
#print(type(a))




#x = {
#    'name': 'saeed',
#    'age': '22',
#    'country': 'india',
 #   'nationality': 'indian'
 #   }
#y = x['name']
#z = x['age']
#print(y)
#print(z)


#x = {
#    'name': 'saeed',
 #   'age': '22',
 #   'country': 'india',
 #   'nationality': 'indian'
  #  }
#y = x.keys()
#print(x)


##x = {
 #   'name': 'saeed',
  #  'age': '22',
#    'country': 'india',
 #   'nationality': 'indian'
 #   }
#y = x.values()
#print(x)


#me = {
#    'name': 'saeed',
#    'age': '22',
#    'country': 'india',
#    'nationality': 'indian'
 #   }
#y = me.values()
#me['name'] = 'sayeed'
#print(me)



#me = {
#    'name': 'saeed',
#    'age': '22',
#    'country': 'india',
#    'nationality': 'indian'
#    }
#me['name'] = 'sayeed'
#print(me)


#me = {
#    'name': 'saeed',
#    'age': '22',
#    'country': 'india',
#    'nationality': 'indian'
#    }
#me.update({'age': '23'})
#print(me)

"""
This is a comment
written in
more than just one line

print("Hello, World!") 
"""


'''
me = {
    'name': 'saeed',
    'age': '22',
    'country': 'india',
    'nationality': 'indian'
    }
me.pop('age')
print(me)
'''

'''
me = {
    'name': 'saeed',
    'age': '22',
    'country': 'india',
    'nationality': 'indian'
    }
for x in me:
    print(x)
'''


'''
x1 = {
  "name" : "saeed",
  "year" : 2022
}
x2 = {
  "name" : "saad",
  "year" : 2023
}
x3 = {
  "name" : "raheem",
  "year" : 2024
}

all = {
  "child1" : x1,
  "child2" : x2,
  "child3" : x3
}

print(all)
'''



















