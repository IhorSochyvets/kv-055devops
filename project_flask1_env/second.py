import requests
import json

# a = input('path: ')
a = "scratch.json"
json_file = open(a)
py_json = json.load(json_file)
res = requests.post('http://localhost:5000/api/add',json=py_json)
print(res.status_code)
# get_response = requests.post('https://api.worldtradingdata.com/api/v1/stock?symbol=AMZN&api_token=0tkx6y1tk3MUvuaNBrye2iIhBACthLoa0gcLHTUSvON2qU7nHKHgmaHMucGn')
# requests.post('https://httpbin.org/post', data={'key':'value'})
# print(get_response.text)
# print(post_resonse.status_code)
