from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:sparta@cluster0.whvqu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.fencat.insert_one(doc)

    return jsonify({'msg':'응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    fen_cats = list(db.fencat.find({}, {'_id': False}))
    return jsonify({'fencat':fen_cats})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)