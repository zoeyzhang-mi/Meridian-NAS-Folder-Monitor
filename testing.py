import requests

my_data = {"sn": {'a':100, 'b': "B"}, 'testdata': 'value2','result': 1}
url='http://192.168.50.131:5000/testing'
#r = requests.post(url, json=my_data, timeout=10)

r = requests.get(url, json=my_data, timeout=10)
print(r.url)
print(f"Status Code: {r.status_code}, Response: {r.json()}")

