import os, ipaddress, whois
import mlq

obj = []
with open('text.txt', 'w+', encoding='utf-8') as f:
    os.system('netstat -tun > text.txt')
    str = f.read().split('\n')
    for i in range(1, len(str)):
        obj.append(str[i].split())
obj.pop(0)
db = ['Giao Thức', 'Server kết nối', 'Nhà cung cấp', 'Địa chỉ ', 'Trạng thái']
imp = []
imp.append(db)

for row in range(0, len(obj)):
    cr = []
    for col in range(0, len(obj[row])):
        if col != 1 and col != 2 and col != 3:
            cr.append(obj[row][col])
        if col == 4:
            try:
                domain = (obj[row][col]).rsplit(':')[0]
                ip_address = int(ipaddress.ip_address(domain))
            except:
                continue
            try:
                domain_gate = whois.whois(domain)['org']
                cr.append(domain_gate)
            except:
                cr.append('None')
            cr.append(mlq.abc(domain))
    imp.append(cr)
imp.pop(-1)
print('+ {:-<20} + {:-^20} + {:-^20} + {:-^60} + {:->20} +'.format('', '', '', '',''))
for i in imp:
    if i[2] is None:
        i[2] = 'None'
    if i[0] != 'tcp6':
        print('| {:^20} | {:^20} | {:^20} | {:^60} | {:^20} |'.format(i[0], i[1], i[2], i[3], i[4]))
print('+ {:-<20} + {:-^20} + {:-^20} + {:-^60} + {:->20} +'.format('', '', '', '', ''))
