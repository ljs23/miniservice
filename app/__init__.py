from flask import Flask


def create_app():
    app = Flask(__name__)

    #环境配置
    app.config.from_object('app.config.DevelopmentConfig')

    return app