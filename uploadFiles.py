import dropbox
import os
from dropbox.files import WriteMode

class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
            print('File Moved.')

def main():
    access_token = '9a3DFX7sHH8AAAAAAAAAARb8WSZXg77UzH-XlEpwP-St8eY36wVWrrVQIfqj9dFX'
    transferData = TransferData(access_token)

    file_from = input('Enter the full path for the file to be uploaded: ')
    file_to = input('Enter the full path to the place to be uploaded: ')

    transferData.upload_file(file_from,file_to)

if __name__ == '__main__':
    main()