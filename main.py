import os, ipaddress, whois
import mlq

obj = []
with open('text.txt', 'w+', encoding='utf-8') as f:
    os.system('netstat -tun > text.txt')
    str = f.read().split('\n')
    for i in range(1,len(str)):
        obj.append(str[i].split())
obj.pop(0)
db = ['Giao Thức','Server kết nối','Nhà cung cấp','Địa chỉ','Trạng thái']
imp = []
imp.append(db)

for row in range(0, len(obj)):
    cr = []
    for col in range(0, len(obj[row])):
        if col != 1 and col != 2 and col != 3:
            cr.append(obj[row][col])
        if col == 4:
            a = False
            domain = (obj[row][col]).rsplit(':')[0]
            ip_address = int(ipaddress.ip_address(domain))
            try:
                domain_gate = whois.whois(domain)['org']
                cr.append(domain_gate)
            except:
                cr.append('None1')
            cr.append(mlq.abc(domain))
    imp.append(cr)
for i in imp:
    print(i)

