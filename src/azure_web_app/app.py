from datetime import datetime

from dotenv import find_dotenv, load_dotenv
from flask import Flask, abort, render_template

from azure_web_app import auth, db
from azure_web_app._constants import SECRET_ENV_FILE


FAVORITES = [
    {"id": 1, "Music": "FAVORITE #1", "why": "How I relax"},
    {"id": 2, "Videogames": "FAVORITE #2", "why": "Play with friends"},
    {"id": 3, "Travel": "FAVORITE #3", "why": "Can explore and learn about new cultures"},
    {"id": 4, "Food": "FAVORITE #4", "why": "I love to eat"},
]

LIFTS = [
    {"id": 1, "name": "bench press", "muscle_group": "chest", "pr": 225, "goal": 275,
     "tip": "Keep your shoulder blades pinched and feet planted."},
    {"id": 2, "name": "squat", "muscle_group": "legs", "pr": 275, "goal": 315,
     "tip": "Brace your core before you descend."},
    {"id": 3, "name": "deadlift", "muscle_group": "back", "pr": 315, "goal": 405,
     "tip": "Keep the bar close to your shins the whole way up."},
    {"id": 4, "name": "overhead press", "muscle_group": "shoulders", "pr": 135, "goal": 155,
     "tip": "Squeeze your glutes so you don't lean back."},
]

def create_app():
    load_dotenv(find_dotenv(SECRET_ENV_FILE))
    app = Flask(__name__)
    db.setup_for_app(app)
    auth.setup_auth(app)
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

def lifts():
    return render_template("lifts.html", lifts=LIFTS)


def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/lifts")(lifts)  


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
