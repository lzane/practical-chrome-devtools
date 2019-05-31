# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 bucketname-appid 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging
import requests
import random
import time
import base64
import hashlib
import hmac
import hashlib
import getopt
from urllib import  parse
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = os.environ['QCLOUD_SECRET_ID']      # 替换为用户的 secretId
secret_key = os.environ['QCLOUD_SECRET_KEY']      # 替换为用户的 secretKey
region = 'ap-guangzhou'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id,
                   SecretKey=secret_key, Token=token, Scheme=scheme)

# 上传文件
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

for path, dir_list, file_list in g:
    if ".git" in path:
        continue
    for file_name in file_list:
        filePath = os.path.join(path, file_name)
        key = filePath[2:]
        myUploadFile(filePath, key)


# 刷新CDN

class CdnHelper(object):
    SecretId = secret_id
    SecretKey = secret_key
    requestHost = 'cdn.api.qcloud.com'
    requestUri = '/v2/index.php?'
    def __init__(self, **args):
        self.type = args['type']
        self.url = args['url']
        self.startDate = args['startDate']
        self.endDate = args['endDate']

    def flushdir_dict(self):
        keydict = {
            'Action': 'RefreshCdnDir',
            'Timestamp': str(int(time.time())),
            'Nonce': str(int(random.random() * 1000)),
            'SecretId': CdnHelper.SecretId,
            'dirs.0': self.url
        }
        sortlist = sorted(zip(keydict.keys(), keydict.values()))
        return sortlist

    def get_str_sign(self):
        if self.type == 'url':
            sortlist = self.flushurl_dict()
        if self.type == 'dir':
            sortlist = self.flushdir_dict()
        sign_str_init = ''
        for value in sortlist:
            sign_str_init += str(value[0]) + '=' + str(value[1]) + '&'
        sign_str = 'GET' + CdnHelper.requestHost + CdnHelper.requestUri + sign_str_init[:-1]
        return sign_str, sign_str_init

    def get_result_url(self):
        sign_str, sign_str_init = self.get_str_sign()
        secretkey = CdnHelper.SecretKey
        signature = bytes(sign_str, encoding='utf-8')
        secretkey = bytes(secretkey, encoding='utf-8')
        my_sign = hmac.new(secretkey, signature, hashlib.sha1).digest()
        my_sign = base64.b64encode(my_sign)
        result_sign = parse.quote(my_sign)
        result_url = 'https://' + CdnHelper.requestHost + CdnHelper.requestUri + sign_str_init + '&Signature=' + result_sign
        return result_url
    def flush_url(self):
        result_url = self.get_result_url()
        try:
            r = requests.get(result_url)
            print(r.json()['codeDesc'])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    tm = datetime.now() + timedelta(hours=-2)
    startDate = endDate = tm.strftime("%Y-%m-%d %H:00:00")
    obj = CdnHelper(type='dir', url='https://devtools.lzane.com', startDate=startDate, endDate=endDate)
    obj.flush_url()