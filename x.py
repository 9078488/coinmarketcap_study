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

# 不错的资源

## 资源1：https://cryptodiffer.com/news/category/hot/
## 资源2：https://www.coingecko.com/zh
## 资源3：https://bc.cnvd.org.cn/ （区块链漏洞子库）
## 资源4：https://grayscale.co/
## 资源5：https://100trillionusd.github.io/index.html  （PlanB）
## 资源6：https://www.lookintobitcoin.com/charts/  （很多比特币价格的图表）
## 资源7：https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/   （2year MA）





