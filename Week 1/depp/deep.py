x = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
x = ''.join(c for c in x if c.isalnum())
if  x == '42' or x == 'fortytwo':
    print('yes')
else:
    print('no')