import requests
import json

url = "https://fanyi.baidu.com/sug"
kw = input("请输入要翻译的内容:")


formData = {
    "kw": kw
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

response = requests.post(url, headers=headers,data=formData)
data = response.text

json_data = json.loads(data)
print(json_data)