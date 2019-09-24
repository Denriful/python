try:
    with open('file1.txt') as file:
        file_data = file.read()
    print(file_data)
except FileNotFoundError:
    print('The datafile is missing.')
except PermissionError:
    print('Does not have permission to read the file.')
#except:
#    print('Some other error.')
except Exception as err:
    print('Some other error: '+str(err))
    