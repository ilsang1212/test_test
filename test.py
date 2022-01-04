import os
import requests
import datetime, random, time
from pymongo import MongoClient
import pymongo, ssl

mongoDB_connect_info : dict = {
    "host" : os.environ["mongoDB_HOST"],
    "username" : os.environ["USER_ID"],
    "password" : os.environ["USER_PASSWORD"]
    }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
url = "https://api-cypress-v2.scope.klaytn.com/v2/accounts/0x908a4e95b447bd2e0fd7c020618ab84b5d6ffc87/ftBalances"

session = requests.Session()
response = session.get(url, headers=headers)
print(session.cookies.get_dict())
print(response)

try:
    price_db = MongoClient(ssl=True, ssl_cert_reqs=ssl.CERT_NONE, **mongoDB_connect_info)
    price_db.admin.command("ismaster") # 연결 완료되었는지 체크
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ndb 연결 완료. 아이디:{mongoDB_connect_info['username']}")
except pymongo.errors.ServerSelectionTimeoutError:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ndb 연결 실패! host 리스트를 확인할 것.")
except pymongo.errors.OperationFailure:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ndb 로그인 실패! username과 password를 확인할 것.")
except:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ndb 연결 실패! 오류 발생:")
