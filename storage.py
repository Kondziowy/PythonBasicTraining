import json

entries = [{"date":"30 May", "text": "Hello world"}, {"date": "1 June", "text": "New discovery"}]

with open("entries.json","w") as f:
  json.dump(entries, f)
with open("entries.json","r") as f:
  restored_entries=json.load(f)
print("After restore")
print(restored_entries)