from azure.storage.blob import BlobServiceClient

st_ac_key="UWE+6aKLze1JoYMBPUUCRPQ2jyBafc2vRflu2cP3nAqTFjzY9t/ATqhx79Eleg+NkXoAHg6byWAa+AStyA6Kxw=="
st_ac_name="cnproject"
con_str="DefaultEndpointsProtocol=https;AccountName=cnproject;AccountKey=d3Pj/eYUGNg88UBq3abvRcfVFRb/UiUMDu5Cn/lGsedaqsioJ1t53sI5YHzMM74tX3yqnqZYVQK3+AStvHzGHg==;EndpointSuffix=core.windows.net"
cont_name="cloud"




def uploadfile(filepath,filename):
    bsc=BlobServiceClient.from_connection_string(con_str)
    bc=bsc.get_blob_client(container=cont_name,blob=filename)
    
    with open(filepath,"rb") as data:
        bc_blob(data)
        
    print("file is uploaded")

uploadfile('D:\\file.txt','awfile')