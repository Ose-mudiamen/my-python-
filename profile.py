import json

profile = {
    "name": "Benjay",
    "Skills": ["Python","Git","CLI"],
    "active": True
}
file = open("profile.json","w")
json.dump(profile,file, indent = 2)
file.close()
print("Saved!")

file = open("profile.json","r")
loaded = json.load(file)
print(loaded["Skills"])
print(loaded["Skills"][1])
print(loaded["active"])
