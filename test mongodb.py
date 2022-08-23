from flask import Flask,request,jsonify
import pymongo

app=Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://maniab123:Mani12345@cluster0.euo4x6n.mongodb.net/?retryWrites=true&w=majority")
#db = client.test

database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo",methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("successfully insert"))


@app.route("/update",methods=['POST'])
def update():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        collection.update_one({'name':'mani'},{'$set':{'name':'nani'}})
        return jsonify(str("updated successfully"))

if __name__=='__main__':
    app.run(port=5001)