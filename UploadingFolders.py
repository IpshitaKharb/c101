import dropbox
import os

class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for file_name in files :
                local_path = os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                     dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BCJdoOU1JrMGW7zWGGq8n1v2eeJpz91Fyg8J0WvMVn7ijkpt7O3TBExYVCU_rR8AUVwZ9aoniNZw0sN1nbVdrMEnTg_0qdVzpaOHlwv6UkbU5CbK4BsZM2mddig3-VoQU64rxP8'
    transferdata = Transferdata(access_token)
    file_from = input("Enter the file name to be transfered")
    file_to = input("Enter the destinatrion where your file should be placed")

    transferdata.upload_file(file_from,file_to)

    print("file moved")

main()

