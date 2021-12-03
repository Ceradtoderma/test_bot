import requests

url = 'https://web-zoopark.ru/wp-content/uploads/2018/06/1-668-700x450.jpg'

res = requests.get(url)

f = open('img.jpeg', 'wb')
f.write(res.content)
f.close()


# print(res.content)