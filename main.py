import os
import logging
import boto3
from botocore.exceptions import ClientError
from PIL import Image
import smtplib
import imghdr
from email.message import EmailMessage
import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random
import hybrid
import time
from azure.storage.blob import BlobServiceClient

st_ac_key="UWE+6aKLze1JoYMBPUUCRPQ2jyBafc2vRflu2cP3nAqTFjzY9t/ATqhx79Eleg+NkXoAHg6byWAa+AStyA6Kxw=="
st_ac_name="cnproject"
con_str="DefaultEndpointsProtocol=https;AccountName=cnproject;AccountKey=d3Pj/eYUGNg88UBq3abvRcfVFRb/UiUMDu5Cn/lGsedaqsioJ1t53sI5YHzMM74tX3yqnqZYVQK3+AStvHzGHg==;EndpointSuffix=core.windows.net"
cont_name="cloud"



#upload
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#menu
print("Welcome to the ‘Student Nest’ platform. The platform has been built to assist to whenever there is any requirement from any faculty regarding class notes, practice questions, mock assignments etc. by the students.")
print()
print("This platform makes sure faculty and students can securely access the cloud driven platform to upload important materials and question papers and to download them whenever needed, respectively.")
print()
print ("# Press 1 if you are a teacher and wish to upload a file")   
print("# Press 2 if you want to download some file of your own cloud")
print()  
print ("# other key to exit")
op=int(input())
if (op == 1):
    filename=input("name the file for cloud storage: ")
    try:
        hybrid.main(filename)
        def uploadfile(filepath,filename):
            bsc=BlobServiceClient.from_connection_string(con_str)
            bc=bsc.get_blob_client(container=cont_name,blob=filename)
            with open(filepath,"rb") as data:
                bc.upload_blob(data)    
            print("file is uploaded")
        uploadfile('D:\\(AES - RSA)\\sender.txt',filename)
    except:
        print ("problem in connections")
elif (op == 2):
    filename=input("name the file you want to download from cloud storage: ")
    try:
        def downloadfile(filepath,filename):
            bsc=BlobServiceClient.from_connection_string(con_str)
            bc=bsc.get_blob_client(container=cont_name,blob=filename)
    
            with open(filepath,"wb") as data:
                data.write(bc.download_blob().readall())
        
            print("file is downloaded in receive.txt")

        downloadfile('D:\\(AES - RSA)\\receive.txt',filename)
    except:
        print("Not able to connect")
else:
    os._exit(0)
    
    