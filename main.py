from random import randint
from flask import Flask, redirect
import episodes as e


def generate_random_episode(start: int, end: int):
    random_season: int = randint(start, end)
    random_episode: int = randint(1, len(e.seasons[random_season]))
    generated_episode: str = e.seasons[random_season][random_episode]
    return f"season {random_season} episode {random_episode}: {generated_episode}"


app = Flask(__name__)


@app.get("/")
def re_route():
    return redirect("/random")


@app.get("/random")
def random():
    return generate_random_episode(1, 25)


@app.get("/random/season/<int:specific_season>")
def season(specific_season):
    return generate_random_episode(specific_season, specific_season)


@app.get('/random/between/<int:start>-<int:end>')
def between(start, end):
    return generate_random_episode(start, end)


if __name__ == '__main__':
    app.run()
