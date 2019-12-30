import flask
from infrastructure.view_modifiers import response
import services.help_service as help_service

blueprint = flask.Blueprint("help", "__name__", template_folder = "templates")

@blueprint.route("/<path:topic_name>")
@response(template_file="/help/help_main.html")
def help(topic_name: str):
    print(f"getting help for {topic_name}")   
    topic = help_service.get_topic(topic_name)
    if not topic:
        return flask.abort(404)

    return topic