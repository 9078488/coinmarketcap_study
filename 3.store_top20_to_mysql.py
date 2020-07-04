import pymysql

db = pymysql.connect('localhost', 'root', '158216dl', 'crypto_price')
cursor = db.cursor()

# 如下这条需要换
original = ['2020-07-04', 'BTC', 'ETH', 'USDT', 'XRP', 'BCH', 'BSV', 'LTC', 'ADA', 'BNB', 'EOS', 'CRO', 'XTZ', 'LINK', 'XLM', 'LEO', 'TRX', 'XMR', 'USDC', 'HT', 'NEO']
sql = """INSERT INTO top20 (
         dates,
         cmc_rank_1,  cmc_rank_2,  cmc_rank_3,  cmc_rank_4,  cmc_rank_5,  cmc_rank_6,  cmc_rank_7,  cmc_rank_8,  cmc_rank_9,  cmc_rank_10,
         cmc_rank_11, cmc_rank_12, cmc_rank_13, cmc_rank_14, cmc_rank_15, cmc_rank_16, cmc_rank_17, cmc_rank_18, cmc_rank_19, cmc_rank_20)
         VALUES
         ('%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',
          '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s',        '%s')"""%(
          original[0],
          original[1], original[2], original[3], original[4], original[5], original[6], original[7], original[8], original[9], original[10],
          original[11], original[12], original[13], original[14], original[15], original[16], original[17], original[18], original[19], original[20])
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()

