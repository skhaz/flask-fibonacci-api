from flask import Flask

from app.blueprints.fibonacci import blueprint as fibonacci_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(fibonacci_blueprint, url_prefix="/")

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
