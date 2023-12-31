import requests
import json
import sys

# 测试程序，接受一个或两个参数
# 参数1 opt:add，list， del
# 参数2： add时， todo的文本
# list ， N/A
# del ， todo_id{0, 1, 2...}
opt = sys.argv[1]
headers = {
    "Content-Type": "application/json"
}
if opt == "add":
    todo = sys.argv[2]
    data = {
        "todo": todo
    }
    response = requests.post("http://127.0.0.1:5002/todos/john", headers=headers, data=json.dumps(data))
if opt == "list":
    response = requests.get("http://127.0.0.1:5002/todos/john", headers=headers)
if opt == "del":
    _id = int(sys.argv[2])
    data = {
        "todo_idx": _id
    }
    response = requests.delete("http://127.0.0.1:5002/todos/john", headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.content)
print(response)
