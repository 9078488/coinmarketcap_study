import pymysql

db = pymysql.connect('localhost', 'root', '158216dl', 'crypto_price')
cursor = db.cursor()

sql = "SELECT * FROM crypto_price_table"
""

original_top_20_2020_06_19 = []

cursor.execute(sql)
results = cursor.fetchall()
# 如下result加1
for item in results[26][1:21]:
	print(item)
	original_top_20_2020_06_19.append(item.split('_')[1])
	print('*' * 100)

# 如下result加1
original_top_20_2020_06_19.insert(0, results[26][1].split('_')[4][0:10])
print(original_top_20_2020_06_19)

db.close()



