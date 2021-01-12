from flask import Flask, redirect, url_for, render_template, request, jsonify
from apps.stock_scraper import scraper

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/", methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return render_template('post.html', content=scraper(variable))


@app.route('/secret')
def secret():
    return render_template("page.html")
    
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    print(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}!'
#
#
# @app.route('/admin/')
# def admin():
#     return redirect(url_for("user", name='admin'))
#
