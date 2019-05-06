import mysql.connector, ipaddress, os, whois
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="ip2location"

)
mycursor = mydb.cursor()
def abc(domain):
    ip_address = int(ipaddress.ip_address(domain))
    ip = "select country_name,region_name,city_name from ip2location_db5 where ip_from = {} or ip_to = {}"
    mycursor.execute(ip.format(ip_address, ip_address))
    myresult = mycursor.fetchall()
    if myresult == []:
        return "Not Found"
    else:
        for i in myresult:
            b = []
            for item in i:
                b.append((item.decode('utf-8')))
            c = ', '.join(b)
        return c
