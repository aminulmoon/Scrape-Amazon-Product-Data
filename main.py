import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0CRDCXRK2/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'cookie': 'x-amz-captcha-1=1709828035222723; x-amz-captcha-2=3g9zGQ/6JtXActKXFo0GKg==; session-id=144-2567883-5729121; ubid-main=135-6534659-0906203; sid="v0pxdeQkKjQLVcJlvuk8zA==|TWvC3R2gQMF0ZFoReIfMOx+LMP5RvZjoi6LtQz8kksE="; x-main="O7nhC7uvNckSbhLX@IgfRRDq7ARscylywHW9Iqyh1Gtsfxh6LffRYOmvRm3nUbgA"; at-main=Atza|IwEBIN5Kbvgl78ovPCqfFBUSEvZH_sHS87TDwp-yqA6oLWMkiwiqwgo7GWx68lYc-UEmqrBa_DWJYmvzaXUI7ra3vdltk9HUAkmlXKWK0o17fO366N27mWtxZR3j1xaZtXNhvyPdSoTq-MYx73NreebTwYdEdKHLmj7w2w_QPjfl5IU29ORLHG0gj5QqssEez0EB0lossuFjkbi7syXtrY06tMUBCe66roA266Gp8HRz2bpJ09vOfTmC0jRW2LNzESz0cMVIjMKEqNdO_ew_cI0oWG07xSnPZ4lXwUp0Fr0Ux_NlvQ; sess-at-main="xIoMCcdmBHQAFFS0JRzrzwVUM7XIm7bq47/g3RmJ5NY="; sst-main=Sst1|PQE-Kb82_khiAKoMYg5nYpMLCUV79ro-9GuVa0OkRnen_jiJDw_-Qkj5y_JL-O-qT3d1ATnJKt0AnLOp-O1fK8Tp7suOrY3ocG4k5_NqlevGnpj23zdnb6VMJxlCfWtPOSJCo_ZI6pQ7o82ITs6vyWj-bzPFUTIMoRNLGmUWVwiKPrMX_7wwetkyZPS4WYGIsFqfOmmvYR8Pe7hU5kMWD6G3vtkCC1PFAgyE0dDdJLSvEqYxO776ONNaWWEHnKfkOXlbBXMubQ2a5KF7vPN_BaB6-bxzGNLheC452Lx5C7oKxkU; lc-main=en_US; i18n-prefs=USD; s_fid=62F608616BD5FF39-2F5EA05E3D3C85D8; session-id-time=2082787201l; av-profile=cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTJTWE9FSUpVWEpJRkgmdGltZXN0YW1wPTE3MjM4NDgwMjYyNzEmdmVyc2lvbj12MQ.gwtDHUtqWNivYoHRmLSu9lxNDptuMz_s2N355sMLtPykAAAAAQAAAABmv9VacmF3AAAAAPgWC9WfHH8iB-olH_E9xQ; av-timezone=Asia/Dhaka; session-token=pxIMM0gUgCxdU1r2p1zujjSxYacjAf1MFlz2cyMlSRKuhyorSEsBpKYuf9b10nu6bDK0EXDXN+uZwxZ+dncZPVIf8Ha1tNAWTxVhCkcxWrehMlLzqTdBIC61tx8/b26EEX4fBq/h93OP4IZJmlp3QkIi9KfIxgD1QR1Xv1JjZrGBIwbFhxP0pO3ZRGHkIXH5KjeHMSJU2sykIkjGO6nUAL/zwdRHDHYzxU9MwUaUrDchlrvEtFL8IVPRoBQ3rHhrIKpAlQXH3N2t0pUZ+eb6LuxWjTi1rPpUeTmniE1/ja5z0JZzha1txD/wFVe8uBHtnoMIvzz4wNUu4Z+H7Ld5StxdJdvucSixvEbyUDNaRCkTsOe4B1tGOfF4srnuv2RT; skin=noskin; csm-hit=tb:s-5YF3RZH5TTED9X6E0VPT|1725418605535&t:1725418606246&adb:adblk_no'
}
res = requests.get(url, headers=headers)
soup = bs(res.text, 'html.parser')

product_title = soup.find('h1', {'id':'title'}).text.strip()

product_table_datas = soup.find('table', {'class':'a-normal a-spacing-micro'})
table_rows = product_table_datas.findAll('tr')

product_table = {}
for table_row in table_rows:
    table_datas = table_row.findAll('td')
    if len(table_datas) ==2:
        product_table[table_datas[0].text.strip()] = table_datas[1].text.strip()


pprint(product_table)