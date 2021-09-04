import requests


url = "https://www.baidu.com"
# 通过get请求
r = requests.get(url)
# 输出服务器状态码
print(r.status_code)
# 输出返回的文本
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(r.text)
print("===================")

# 通过post方法
data = {
    "username": "123",
    "password": "123"
}
r = requests.post(url, data=data)
print(r.text)
