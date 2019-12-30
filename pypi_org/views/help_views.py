import flask
from infrastructure.view_modifiers import response

blueprint = flask.Blueprint("help", "__name__", template_folder = "templates")

@blueprint.route("/help/<topic_name>")
#@response(template_file="details.html")
def help(topic_name: str):
    #topic = db.get_topic(topic_name)
    return f"this is a place holder for help with {topic_name}"