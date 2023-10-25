file =  input('File name: ')
if '.' in file:
    name, extension = file.rsplit('.',maxsplit=1)
    match extension.lower().strip():
        case 'gif':
            print('image/gif')
        case 'jpg':
            print('image/jpeg')
        case 'jpeg':
            print('image/jpeg')
        case 'png':
            print('image/png')
        case 'pdf':
            print('application/pdf')
        case 'txt':
            print(f'text/{name}')
        case 'zip':
            print('application/zip')
        case _:
            print('application/octet-stream')
else:
    print('application/octet-stream')
