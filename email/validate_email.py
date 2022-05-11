import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
'diguinhogamerbr10@gmail.com'
def valid(pattern):
    email = input('input your email: ')
    if re.search(pattern, email):
        print('email cadastrado!')
    else:
        print('pxii, tenta dnv q n foi n')
        valid(pattern) 

valid(pattern)