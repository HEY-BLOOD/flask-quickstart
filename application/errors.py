from application import app
from flask import render_template
from werkzeug.exceptions import HTTPException, InternalServerError

# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     import json
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response


@app.errorhandler(Exception)
def handle_exception(e):
    """通用异常处理器"""
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return render_template("error.html", error=e), e.code

    # now you're handling non-HTTP exceptions only
    # 500 异常不属于HTTP错误
    return render_template("error.html", error=e), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e), 404
