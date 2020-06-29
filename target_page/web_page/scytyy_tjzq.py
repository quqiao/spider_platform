import requests
from bs4 import BeautifulSoup

def login():
    login_url = 'http://www.scytyy.net/login.html'
    headers = {'Host': 'www.scytyy.net',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
               }
    body = {
        'username': '18030535053',
        'userpass': '123456',
        'do': 'login'
    }
    try:
        res = requests.post(url=login_url, headers=headers, data=body)
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie
    except Exception as err:
       print('获取cookie失败：\n{0}'.format(err))

def get_data():
    cookie = login()
    headers = {'Host': 'www.scytyy.net',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
               }
    get_url = 'http://www.scytyy.net/activitypage2.php'
    body = {
        'page': '1',
        'ajaxid': '627'
        }
    res = requests.post(url=get_url, data=body, headers=headers, cookies=cookie)
    print(res.text)
    return res.text

def crawl_scytyy():
    soup = BeautifulSoup(get_data(), 'lxml')
    jg = soup.find_all(class_="price_1")
    mz = soup.find_all(class_="l_ty")
    cj = soup.find_all('li')
    cj1 = cj[0]
    cj2 = cj1.find_parents('ul')


if __name__ == '__main__':# 验证拼接后的正确性
    print(login())
    print(get_data())