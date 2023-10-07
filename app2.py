from flask import Flask, jsonify, request

app = Flask(__name__) 
tasks = [
    {
        'id':1,
        'contact':'1234567890',
        'name':'Bob',
        'done':False
    },
    {
        'id':2,
        'contact':'0987654321',
        'name':'Milo',
        'done':False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"problem arising because the request was not recived"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"good",
        "message":"it worked"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__ == "__main__"):
    app.run(debug=True)