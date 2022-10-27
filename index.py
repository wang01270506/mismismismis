from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411003811 王思婷的求職相關資訊</h1>"
    homepage += "<a href=/aboutme2>我的個人簡介</a><br>"
    homepage += "<a href=/company>MIS相關工作介紹</a><br>"
    homepage += "<a href=/ucan>職涯測驗結果</a><br>"
    homepage += "<a href=/sun>求職履歷自傳</a><br>"
    return homepage

@app.route("/aboutme2")
def aboutme2():
    now = datetime.now()
    return render_template("aboutme2.html", datetime = str(now))

@app.route("/company")
def company():
    now = datetime.now()
    return render_template("company.html", datetime = str(now))

@app.route("/ucan")
def ucan():
    now = datetime.now()
    return render_template("ucan.html", datetime = str(now))
    
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/sun")
def sun():
    now = datetime.now()
    return render_template("sun.html", datetime = str(now))


if __name__ == "__main__":
    app.run()
