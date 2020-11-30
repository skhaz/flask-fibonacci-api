from flask import Blueprint, abort, make_response, request


from app.helpers import safe_cast
from app.fibonacci import fibonacci, is_valid

blueprint = Blueprint("fibonacci", __name__)


@blueprint.route("/fib")
def fib():
    raw = request.args.get("n")

    number = safe_cast(raw)

    if not is_valid(number):
        abort(400)

    result = fibonacci(number)

    response = make_response(str(result), 200)
    response.mimetype = "text/plain"
    return response
