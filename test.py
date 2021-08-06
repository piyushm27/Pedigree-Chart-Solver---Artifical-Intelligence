import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print sys.argv[0]

'''
listoflists = []
alist = []
for i in range(0,10):
    alist.append(i)
    if len(alist)>3:
        alist.remove(alist[0])
        listoflists.append((list(alist), alist[0]))
print (listoflists)

for list in listoflists:
    print(list[0])

for i in range(7,8):
    print(i)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
y={k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(y)
my_dict = {(0,1):500, (1,3):5874, (5,6): 560}
for key in my_dict:
    print(key)
n_list=[]
print("\n")
while len(my_dict)!=0:
    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    print(key_max)
    n_list.append(key_max)
    del my_dict[key_max]
print("\n")
print(my_dict)
for key in n_list:
    print(key)
'''