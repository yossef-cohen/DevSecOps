from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/moshe")
def hello_moshe():
    return "Moshe is a nice boy."

@app.route('/', methods= ['POST'])
def save_data():
    print(request.data)
    return "saved"

names = ""
users = {}

@app.route("/name", methods=['GET', 'POST'])
def name():
    global names
    if request.method == 'POST':
        names = request.get_json()
        return f"Name saved: {names['name']}\n"
    else:
        if names == "":
            return "Name not saved"
        else:
            return f"The Name is: {names['name']}\n"

@app.route("/user", methods=['GET', 'POST', 'DELETE', 'PUT'])  
def user():
    global users
    search = request.get_json()
    ids = search.get("id")
    name = search.get("name")
    phone = search.get("phone")

    if request.method == 'POST':
        users[ids] = request.get_json()
        return f"{users[ids]}\n"
    elif request.method == 'PUT':
        users[ids] = {"name": name, "phone": phone}
        return f"User updated: ID: {ids}, Name: {name}, Phone: {phone}\n"
    else:
        for id in users:
            if (name and users[id]["name"] == name) or (phone and users[id]["phone"] == phone):
                if request.method == 'GET':
                    return f"User found: Name: {users[id]['name']}, Phone: {users[id]['phone']}\n"
                elif request.method == 'DELETE': 
                    users.pop(id)
                    return f"User deleted: Name: {name}, Phone: {phone}\n"

        return "User not found\n"

app.run()
