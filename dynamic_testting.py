from flask import redirect, request, render_template, url_for, Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("post.html")

if __name__ == '__main__':
    app.run(debug=True)
