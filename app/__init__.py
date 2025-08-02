from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.login import login_bp
    from app.routes.home import home_bp
    from app.routes.compraempresas import compra_bp
    from app.routes.gastoempresas import gasto_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(compra_bp)
    app.register_blueprint(gasto_bp)

    return app
