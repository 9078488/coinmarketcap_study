import pymysql

db = pymysql.connect("localhost", "root", "158216dl", "crypto_price")
cursor = db.cursor()

sql = "SELECT * FROM top20"

top20_list = []

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
    	for item in result[2:]:
    		top20_list.append(item)
except:
	print("Error")



db.close()


print(set(top20_list))
print(len(set(top20_list)))