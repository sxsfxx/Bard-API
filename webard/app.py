from bardapi import Bard
from flask import Flask
from flask import request
from flask import render_template

token = 'YwgC030KE0JFi41YY9iqOJ44y6uuKjZSQz6g8FEFMKmIY8SicAYQBLAlMv-A4yD6RjE23A.'
bard = Bard(token=token)
#s = bard.get_answer("请告诉我世界上最高的山峰是哪一个？")['content']
#print(s)

app = Flask(__name__)

kvs = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        if q:
            try:
                a = bard.get_answer(q)["content"]
                if a:
                    kvs.update({q:a})
            except:
                kvs.update({q:"error"})
    return render_template("index.html", kvs=kvs)
