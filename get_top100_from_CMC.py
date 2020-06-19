from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pandas import DataFrame
import pandas as pd

print('start')

url = 'https://pro-api.coinmarketcap.com//v1/cryptocurrency/listings/latest'
parameters = {
  'start': 1,
  'limit':100
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5fa53146-23a7-450f-ad6d-eef06dfdb897',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)



except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



res = data['data']

ll = []

for i in res:
	zz = str(i['cmc_rank']) + '_' + i['symbol'] + '_' + str(i['quote']['USD']['price']) + '_' + str(i['quote']['USD']['market_cap']) + '_' + str(i['last_updated'])
	print(zz)
	eee = zz.split('_')
	print(eee)
	ll.append(zz)
	print('-' * 100)

print(ll)





import pymysql

db = pymysql.connect('localhost', 'root', '158216dl', 'crypto_price')

cursor = db.cursor()

sql = """INSERT INTO crypto_price_table
         (cmc_rank_1,  cmc_rank_2,  cmc_rank_3,  cmc_rank_4,  cmc_rank_5,  cmc_rank_6,  cmc_rank_7,  cmc_rank_8,  cmc_rank_9,  cmc_rank_10,
          cmc_rank_11, cmc_rank_12, cmc_rank_13, cmc_rank_14, cmc_rank_15, cmc_rank_16, cmc_rank_17, cmc_rank_18, cmc_rank_19, cmc_rank_20,
          cmc_rank_21, cmc_rank_22, cmc_rank_23, cmc_rank_24, cmc_rank_25, cmc_rank_26, cmc_rank_27, cmc_rank_28, cmc_rank_29, cmc_rank_30,
          cmc_rank_31, cmc_rank_32, cmc_rank_33, cmc_rank_34, cmc_rank_35, cmc_rank_36, cmc_rank_37, cmc_rank_38, cmc_rank_39, cmc_rank_40,
          cmc_rank_41, cmc_rank_42, cmc_rank_43, cmc_rank_44, cmc_rank_45, cmc_rank_46, cmc_rank_47, cmc_rank_48, cmc_rank_49, cmc_rank_50,
          cmc_rank_51, cmc_rank_52, cmc_rank_53, cmc_rank_54, cmc_rank_55, cmc_rank_56, cmc_rank_57, cmc_rank_58, cmc_rank_59, cmc_rank_60,
          cmc_rank_61, cmc_rank_62, cmc_rank_63, cmc_rank_64, cmc_rank_65, cmc_rank_66, cmc_rank_67, cmc_rank_68, cmc_rank_69, cmc_rank_70,
          cmc_rank_71, cmc_rank_72, cmc_rank_73, cmc_rank_74, cmc_rank_75, cmc_rank_76, cmc_rank_77, cmc_rank_78, cmc_rank_79, cmc_rank_80,
          cmc_rank_81, cmc_rank_82, cmc_rank_83, cmc_rank_84, cmc_rank_85, cmc_rank_86, cmc_rank_87, cmc_rank_88, cmc_rank_89, cmc_rank_90,
          cmc_rank_91, cmc_rank_92, cmc_rank_93, cmc_rank_94, cmc_rank_95, cmc_rank_96, cmc_rank_97, cmc_rank_98, cmc_rank_99, cmc_rank_100)
         VALUES
         ('%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s')"""%(
           ll[0],       ll[1],       ll[2],       ll[3],       ll[4],        ll[5],       ll[6],       ll[7],       ll[8],       ll[9],
           ll[10],      ll[11],      ll[12],      ll[13],      ll[14],       ll[15],      ll[16],      ll[17],      ll[18],      ll[19],
           ll[20],      ll[21],      ll[22],      ll[23],      ll[24],       ll[25],      ll[26],      ll[27],      ll[28],      ll[29],
           ll[30],      ll[31],      ll[32],      ll[33],      ll[34],       ll[35],      ll[36],      ll[37],      ll[38],      ll[39],
           ll[40],      ll[41],      ll[42],      ll[43],      ll[44],       ll[45],      ll[46],      ll[47],      ll[48],      ll[49],
           ll[50],      ll[51],      ll[52],      ll[53],      ll[54],       ll[55],      ll[56],      ll[57],      ll[58],      ll[59],
           ll[60],      ll[61],      ll[62],      ll[63],      ll[64],       ll[65],      ll[66],      ll[67],      ll[68],      ll[69],
           ll[70],      ll[71],      ll[72],      ll[73],      ll[74],       ll[75],      ll[76],      ll[77],      ll[78],      ll[79],
           ll[80],      ll[81],      ll[82],      ll[83],      ll[84],       ll[85],      ll[86],      ll[87],      ll[88],      ll[89],
           ll[90],      ll[91],      ll[92],      ll[93],      ll[94],       ll[95],      ll[96],      ll[97],      ll[98],      ll[99])
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print('OK')
except:
   # 如果发生错误则回滚
   db.rollback()
   print('wow')
