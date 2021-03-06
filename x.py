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

## 资源1：https://cryptodiffer.com/news/category/hot/   (无API)
## 资源2：https://www.coingecko.com/zh (有价格API)
## 资源3：https://bc.cnvd.org.cn/ （区块链漏洞子库）
## 资源4：https://grayscale.co/
## 资源5：https://100trillionusd.github.io/index.html  （PlanB）
## 资源6：https://www.lookintobitcoin.com/charts/  （很多比特币价格的图表）
## 资源7：https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/   （2year MA）
## 资源8：https://glassnode.com/
## 资源9：https://coinmetrics.io/
## 资源10: https://research.arcane.no/
## 资源11: https://www.cryptocompare.com/
## 资源12: https://www.kaggle.com/
## 资源13: https://tokeninsight.com/
## 资源14: https://www.intotheblock.com/
## 资源15: https://tokenview.com/
## 资源16: https://www.tradingview.com/chart/
## 资源17: https://coinstats.app    (有history api)
## 资源18: https://www.theblockcrypto.com/
## 资源19: https://ahr999.com/
## 资源20: https://www.qkl123.com/
## 资源21: https://www.aicoin.cn/
## 资源22: https://santiment.net/
## 资源23: https://cointelegraph.com/
## 资源24: https://dappradar.com/
## 资源25: https://defipulse.com/
## 资源26: https://www.longhash.com/cn
## 资源27: https://block.info/index
## 资源28: https://chainext.io/home
## 资源29: http://deepdao.io/
## 资源30: https://www.delphidigital.io/
## 资源31: https://www.burgercrypto.com/
## 资源32: https://www.coindesk.com/ (找下coindesk 20)




