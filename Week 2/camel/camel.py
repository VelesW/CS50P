camel = input('camelCase: ')
table = [camel[0].lower()]
for c in camel[1:]:
    if c.isupper():
        table.append('_')
        table.append(c.lower())
    else:
        table.append(c)
snake = ''.join(table)
print(f'snake_case: {snake}')