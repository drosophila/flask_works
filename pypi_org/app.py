import flask

from infrastructure.view_modifiers import response
import services.package_service as package_service
app = flask.Flask(__name__)


@app.route("/")
@response(template_file="/home/index.html")
def index():
    test_packages = package_service.get_latest_packages()
    return {"packages":test_packages}

@app.route("/about")
@response(template_file="/home/about.html")
def about():
    return {}

if __name__ == "__main__":
    app.run(debug = True) 