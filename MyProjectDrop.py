import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)
                relativePath = os.path.relpath(local_path, file_from)
                dropboxPath = os.path.join(file2, relativePath)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath)

def main():
    access_token = input('Enter Access Token: ')
    transferData = TransferData(access_token)
    file_from = input('Enter File That You Want To Transfer: ')
    file_to = input('Enter Dropbox Location: ')
    transferData.uploadFiles(file_from, file_to)
    print('File has been moved')

move()