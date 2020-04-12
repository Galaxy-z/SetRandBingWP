import requests
import os.path
import ctypes
import json

# 获得壁纸
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69'
}
url = 'https://bing.ioliu.cn/v1/rand?callback=json'
page = requests.get(url, headers=headers)
imgurl = json.loads(page.text.split(' json')[2][1:-2])['data']['url']
img = requests.get(imgurl, headers=headers).content
# 保存图片
imgname = 'bingwallpaper.jpg'
with open(imgname, 'wb') as f:
    f.write(img)
# 设置壁纸
filepath = os.path.abspath(imgname)
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
