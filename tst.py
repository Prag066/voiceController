import os

# path = '/home/prakhar/PycharmProjects/test/'
# def check():
#     path1 = path
#     for name in os.listdir(path):
#         if os.path.isdir(name):
#             path1 = path + name
#             if path1:
#                 for i in os.listdir(path1):
#                     print(i)
# check()

path = '/home/prakhar/vc/'
os.chdir(path)
for roots,dirs,files in os.walk(path):
    for f in files:
        if 'tst.py' in f:
            print('yes')
            print(path+f)
            break
        else:
            pass
    # print(files)
