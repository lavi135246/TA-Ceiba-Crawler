# TA-Ceiba-Crawler
NTU ceiba homework crawler

## Requirements
- python 3
- Google Chrome (I was using: 77.0.3865.120-1)
- selenium
- PyVirtualDisplay


```bash
$ pip install selenium PyVirtualDisplay parsing 
$ sudo apt-get install xvfb
```
#### Chrome driver
```bash
# you may also search for the driver version for your chrome version here
# http://chromedriver.storage.googleapis.com/index.
# I was using 77.0.3865.10
$ wget -N http://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ chmod +x chromedriver
$ sudo mv -f chromedriver /usr/local/share/chromedriver
$ sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

## How it works
```bash
$ python HWcrawler.py
# 1. 作業下載路徑
# 2. 請輸入 ceiba 帳號 (TA)
# 3. 請輸入 ceiba 密碼
# 4. 請輸入作業編號 
```

![image](./homework_id.PNG)
