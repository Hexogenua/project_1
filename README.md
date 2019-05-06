# project 1

Proto: Giao thức kết nối: tcp/udp Local Address: Địa chỉ máy hiện tại Foreign Address: Địa chỉ server kết nối đến State: Trạng thái kết nối. Chi tiết: http://manpages.ubuntu.com/manpages/cosmic/en/man8/netstat.8.html phần State

Viết 1 chương trình python, chạy lệnh netstat để lấy output xong chuyển đổi sang dạng dễ đọc hơn theo cấu trúc:

Giao thức - Server kết nối - Nhà cung cấp - Địa chỉ - Trạng thái

Trong đó:

Giao thức: TCP hoặc UDP

Server kết nối: Gồm IP, Port

Nhà cung cấp: OrgName của IP (gõ lệnh whois <ip> để xem). Có thể dùng các thư việc whois của python để lấy, để chạy nhanh thì sau mỗi lần whois 1 domain mới thì lưu lại vào db, từ lần sau trở đi thì lấy luôn trong db.

Địa chỉ: Gồm city name, region name, country name. Lấy thông tin ở db này: https://lite.ip2location.com/database/ip-country-region-city-latitude-longitude. Download về , rồi dùng.

VD:

Giao thức - Server kết nối     - Nhà cung cấp - Địa chỉ                                 - Trạng thái

TCP         64.233.188.189:443   Google LLC     Mountain View, California, United States  ESTABLISHED

Db dùng sql
