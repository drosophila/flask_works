import flask
from infrastructure.view_modifiers import response
#import services.package_service as package_service

blueprint = flask.Blueprint("packages", "__name__", template_folder = "templates")

@blueprint.route("/project/<package_name>")
#@response(template_file="details.html")
def package_details(package_name: str):
    return f"pacakge detail for {package_name}"

@blueprint.route("/<int:rank>")
def popular(rank: int):
    if rank==1:
        return "The details for the #1 most popular package"
    elif rank==2:
        return "The details for the 2nd most popular package"
    else:
        return f"The details for the {rank}th most popular package"
