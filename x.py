import requests

# Get Instant Price
# Source1: FeiXiaoHao
r1 = requests.get('https://fxhapi.feixiaohao.com/public/v1/ticker/')

result1 = r1.json()

print('Price from FeiXiaoHao')
print(result1[0]['id'])
print(result1[0]['symbol'])
print(result1[0]['price_usd'])
print('-' * 100)

# Source2:

r2 = requests.get('https://api.alternative.me/v2/ticker/')

result2 = r2.json()

print('Price from alternative.me')
print(result2['data']['1']['name'])
print(result2['data']['1']['quotes']['USD']['price'])
print('-' * 100)

# Get Fear & Greedy Index

r3 = requests.get('https://api.alternative.me/fng/')

result3 = r3.json()

print(result3['name'])
print(result3['data'][0]['value'])
print(result3['data'][0]['value_classification'])
print('-' * 100)





