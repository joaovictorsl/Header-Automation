import sys
import os

QUESTION_KEY = sys.argv[1]
PROGRAM_DESCRIPTION = sys.argv[2:]

try:
    with open('header.txt', 'r') as file:
        header = file.readlines()
except:
    DEFAULT_HEADER = ['# UFCG - P1\n', '# SEU NOME\n', '# ']
    with open('header.txt', 'w') as file:
        file.writelines(DEFAULT_HEADER)

directories_before = os.listdir()

os.system(f'p1 checkout {QUESTION_KEY}')

directories_after = os.listdir()

for dir in directories_after:
    if not dir in directories_before:
        with open(f'{dir}/{dir}.py', 'w') as file:
            file.writelines(header)
            file.write(' '.join(PROGRAM_DESCRIPTION) + '\n')
        os.system(f'cd {dir};vim {dir}.py')
        exit(0)

