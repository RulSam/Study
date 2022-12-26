# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.content)
# print(r.status_code)

#
# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
# texts = json.loads(r.content)
# print(type(texts))
#
# for text in texts:
#     print(text[:50], "\n")

# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# print(r.content)

# import requests
# import json
#
# r = requests.get('https://api.github.com')
# d = json.loads(r.content)
#
# print(type(d))
# print(d['following_url'])


# Давайте посмотрим, как с помощью уже знакомой нам библиотеки отправить данные в нужном нам формате:
# import requests
# import json
#
# data ={'key': 'value'}
# r = requests.post('https://httpbin.org/post', json=json.dumps(data))
#
# print(r.content)