# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 bucketname-appid 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = os.environ['QCLOUD_SECRET_ID']      # 替换为用户的 secretId
secret_key = os.environ['QCLOUD_SECRET_KEY']      # 替换为用户的 secretKey
region = 'ap-guangzhou'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)

bucket_name = 'devtools-1251731749'

def myUploadFile(filePath, key):
    response = client.upload_file(
        Bucket=bucket_name,
        LocalFilePath=filePath,
        Key=key,
        PartSize=10,
        MAXThread=10,
        EnableMD5=False
    )
    print(response['ETag'])

g = os.walk(r".")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        filePath = os.path.join(path, file_name)
        key = filePath
        myUploadFile(filePath,key)


# # 刷新CDN
# cdn_manager = CdnManager(q)
# dirs = [
#     'https://www.lzane.com/'
# ]
# refresh_dir_result = cdn_manager.refresh_dirs(dirs)
