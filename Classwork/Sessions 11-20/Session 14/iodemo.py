import os
print(os.getcwd())
# f_out = open('Classwork/Session 14/output.txt','w')

# line1 = "How many roads must a man walk down\n"
# f_out.write(line1)

# line2 = "Before you call him a man?\n"
# f_out.write(line2)
# f_out.close()

# with open('Classwork/Session 14/output.txt','w') as f_out:
#     line1 = "How many roads must a man walk down\n"
#     f_out.write(line1)
#     line2 = "Before you call him a man?\n"
#     f_out.write(line2)

# print(os.path.abspath('output.txt'))
# print(os.path.exists('Classwork/Session 14/output.txt'))

# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# def walk2(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))

# walk(os.getcwd())

# try:
#     fin = open('bad_file')
# except FileNotFoundError as e:
#     print('Something went wrong',e)

# with open('bad_file') as f:
#     print(f.read())

import pickle

t = [1, 2, {'Carmen':95, 'Victoria':99}]

# print(pickle.dumps(t))

with open('Classwork/Session 14/saved.p','wb') as p:
    pickle.dump(t,p)

with open('Classwork/Session 14/saved.p','rb') as p:
    t2 = pickle.load(p)

print(t2)
print(t == t2)
print(t is t2)

print(dir(pickle))