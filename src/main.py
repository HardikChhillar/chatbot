from flask import Flask, send_from_directory
from src.routes.chat import setup_chat_route
import os

def create_app():
    app = Flask(__name__, static_folder=None)

    # API
    setup_chat_route(app)

    # Serve UI files (Vercel rewrite will map / to this)
    ui_dir = os.path.join(os.path.dirname(__file__), "ui")

    @app.route("/")
    def index():
        return send_from_directory(ui_dir, "index.html")

    @app.route("/app.js")
    def app_js():
        return send_from_directory(ui_dir, "app.js")

    @app.route("/styles.css")
    def styles_css():
        return send_from_directory(ui_dir, "styles.css")

    return app

# For local dev
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)