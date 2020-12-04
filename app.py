from flask import Flask, redirect, url_for, render_template, request, send_file
import util

# creating instance of Flask
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        keyword = request.form["nm"]
        location = request.form["lc"]
        # return render_template("index.html")
        return redirect(url_for("details", loc=location, key=keyword))
    else:
        return render_template("index.html")


@app.route("/<loc>/<key>")
def details(loc, key):
    link = f"https://www.justdial.com/{loc}/{key}/page-"
    # return f"<h1>{(util.get_details(link))}</h1>"
    fname = key +".csv"
    util.get_details(link)
    return send_file(fname, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    print("RUNNING")
