import requests
from datetime import datetime
from bs4 import BeautifulSoup

line_notify_api = 'https://notify-api.line.me/api/notify'
# xxx → 自分のトークンに変更
line_notify_token = 'xxx'

day = datetime.today()
# xxx → 所属キャンパス・学部のURLに変更
URL = 'http://msgsot.sic.shibaura-it.ac.jp/cancel/xxx/{}.html'.format(
    day.strftime('%Y%m%d'))
URL = 'http://msgsot.sic.shibaura-it.ac.jp/cancel/s06/20171011.html'
resp = requests.get(URL)
if resp.status_code == 200:
    # 文字コード変更
    resp.encoding = resp.apparent_encoding
    # テキスト整形
    soupTemp = BeautifulSoup(resp.text, 'html.parser').body
    # LINE Notify
    print(soupTemp)
    soup = BeautifulSoup(resp.text, 'html.parser').body.get_text('\n', strip=True)
    # LINE Notify
    print(soup)
    payload = {'message': soup}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    # requests.post(line_notify_api, data=payload, headers=headers)
