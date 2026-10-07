from flask import Flask, render_template
from datetime import datetime
from flask import Flask, render_template
from flask import Flask, abort, render_template

FAVORITES = [
    {"id": 1, "Music": "FAVORITE #1", "why": "How I relax"},
    {"id": 2, "Videogames": "FAVORITE #2", "why": "Play with friends"},
    {"id": 3, "Travel": "FAVORITE #3", "why": "Can explore and learn about new cultures"},
    {"id": 4, "Food": "FAVORITE #4", "why": "I love to eat"},
]
def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app


def index():
    return render_template(
        "index.html",
        name="Carson Blaker",
        hobby="Weight lifting",
        hours_per_week=30,  # roughly how many hours a week you spend on it
        fun_fact="I can bench press 225 pounds!",  # a fun fact about yourself
        hour=datetime.now().hour,
        show_counter=True,
        favorites=FAVORITES,
    )

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
