import os

path0 = os.listdir('./223/plugins')

path1 = os.listdir('./123/plugins')

for file in path1:
    if file not in path0:
        print(file)