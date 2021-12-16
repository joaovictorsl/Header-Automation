import sys
import os

with open('header.txt', 'r') as file:
    header = file.readlines()

directories_before = os.listdir()

os.system(f'p1 checkout {sys.argv[1]}')

directories_after = os.listdir()

for dir in directories_after:
    if not dir in directories_before:
        with open(f'{dir}/{dir}.py', 'w') as file:
            file.writelines(header)
            file.write(' '.join(sys.argv[2:]) + '\n')
        exit(0)
