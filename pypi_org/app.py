import flask

app = flask.Flask(__name__)

@app.route("/")
def index(): #the def is the controller referred to as the view method
    test_packages = [
        'package1',
        'package2',
        'package3',
    ]
    return flask.render_template("index.html", packages = test_packages) #index.html is the view or the view template

if __name__ == "__main__":
    app.run(debug = True)