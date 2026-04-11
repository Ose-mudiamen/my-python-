import json
raw = '{"name": "Benjay","course": "Computer Science", "level": 300}'
data = json.loads(raw)

print(data["name"])
print(data["course"])
print(type(data)) 