from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def home():
    posts = [
        {"title": "第一篇","author":"久米"},
        {"title": "第二篇","author":"小红"},
        {"title": "第三篇","author":"小刚"},

    ]
    return render_template("index.html",name="久米",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)