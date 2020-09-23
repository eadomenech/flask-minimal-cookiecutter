from flask import Flask


def create_app(config):
    """Application setup"""
    app = Flask(__name__, instance_relative_config=False)
    # load the config
    app.config.from_object(config)

    # load some plugins, modules or blueprints
    from application.views.default import default

    # registrar los blueprints
    app.register_blueprint(default)

    return app
