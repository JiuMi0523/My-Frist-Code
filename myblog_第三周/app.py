from flask import Flask,render_template,request,redirect
from datetime import datetime
app = Flask(__name__)

posts = [
    
    {"title": "第一篇","author":"久米","content":"第一篇的内容","time":"2026-10-01 09:00"},
    {"title": "第二篇","author":"小红","content":"第二篇的内容","time":"2026-10-01 09:00"},
    

   ]
@app.route("/")    
def home():
    return render_template("index.html",name="久米",posts=posts)

@app.route("/new",methods=["GET","POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get("title")
        author=request.form.get("author")
        content = request.form.get("content")
        if title:
           now = datetime.now().strftime("%Y - %M - %d %H:%M")
           posts.append({"title":title,"author":author,"content":content,"time": now})
        return redirect("/")
    return render_template("new_post.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)