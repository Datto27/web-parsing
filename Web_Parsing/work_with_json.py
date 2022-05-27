import json
user = {
	"username": "John",
	"email": "johndoe@gmail.com"
}
print(json.dumps(user))
with open("result.json", "w") as fp:
	json.dump(user, fp)

