import requests

from 第二章.request基本使用 import headers

url = "https://api.bilibili.com/x/web-interface/nav"

headers ={
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "cookie":"buvid3=09AA434F-35FC-5299-3684-1D8CF40EF68E00689infoc; b_nut=1700057800; _uuid=1CFBE5FF-B3ED-78EC-45BC-6D154C751010F999996infoc; buvid4=359DC6B2-6510-79B2-F5CE-4234DE39A88643436-023121913-KWJiaspPg9Ye4lrPXCbb4g%3D%3D; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=1753032599; DedeUserID__ckMd5=528c20eec5482e3d; rpdid=|(u~JRl~kYmY0J'u~|)mk|kR~; CURRENT_QUALITY=80; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; LIVE_BUVID=AUTO4917164709482718; PVID=2; home_feed_column=4; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjkxNTUwODYsImlhdCI6MTcyODg5NTgyNiwicGx0IjotMX0.To4MTHzdSvLHW0r1F1UxbOvXUUtzaBPco1Jze4hp-rc; bili_ticket_expires=1729155026; SESSDATA=a1b31ae6%2C1744447887%2Cf9b8d%2Aa2CjB30YVtOjHUUttpXKfVnSLWzk3PIgUK9sPu4uzqV5AS42Ltcg1WYyKYlLcn6fhc_NISVkJsNWNsZDBLampwQmNVdmNCLWpKeGxlOUM0cE8xRFViV24tUlNYTzJ6X2hFV1g1dVhaOElZMlJQMVpJaDhYMzQ3emMyNnFsa09zUDBYOVNBTnpiaWNBIIEC; bili_jct=7174906799aa672b051e2a0a383978fe; sid=fntfjanj; b_lsid=66A67267_1928A4E4A50; bsource=search_bing; browser_resolution=1133-234; bp_t_offset_1753032599=988096903352680448; fingerprint=80cdcb537c16dc4f63fb71eb1da9ce22; buvid_fp_plain=undefined; buvid_fp=09AA434F-35FC-5299-3684-1D8CF40EF68E00689infoc"
}

response = requests.get(url,headers=headers)
data = response.json()
print(data["data"]["uname"])
