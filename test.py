import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
url = "https://api-cypress-v2.scope.klaytn.com/v2/accounts/0x908a4e95b447bd2e0fd7c020618ab84b5d6ffc87/ftBalances"

session = requests.Session()
response = session.get(url, headers=headers)
print(session.cookies.get_dict())
print(response)
