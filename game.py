from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
)
import random
import pandas as pd
from dotenv import find_dotenv, load_dotenv
import os


ENV_FILE = find_dotenv(".env")
if ENV_FILE:
    load_dotenv(ENV_FILE)


app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["fish_csv"] = os.getenv("FISH_CSV")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    if "score" not in session:
        session["score"] = 0
    if "rounds_counter" not in session:
        session["rounds_counter"] = 0

    fish_df = pd.read_csv(app.config["fish_csv"], index_col=0)
    real_fish = fish_df[fish_df['real']==True]['name'].to_list()
    made_up_fish = fish_df[fish_df['real']==False]['name'].to_list()

    real_options = random.sample(real_fish, k=3)
    finte = random.sample(made_up_fish, k=1)[0]

    options = real_options + [finte]
    random.shuffle(options)

    correct_index = options.index(finte)
    correct_option = options[correct_index]
    session["correct_option"] = correct_option

    return render_template("game.html", options=options, score=session["score"])


@app.route("/submit", methods=["POST"])
def submit():
    session["rounds_counter"] += 1
    selected_option = request.form.get("option")

    if not selected_option:
        flash("Please select an option.")
        return redirect("/game")

    if selected_option == session.get("correct_option"):
        session["score"] += 1
        flash(f"Correct! {random.choice(['🐟', '🐠', '🐡', '🦈'])}")
    else:
        flash(f"Incorrect! {random.choice(['🎣', '🍣', '🍤'])}")

    print(f"Selected option: {selected_option}, Score: {session['score']}")

    return redirect("/game")


@app.route("/end_game", methods=["GET", "POST"])
def end_game():
    try:
        percentage_correct = (session["score"] / session["rounds_counter"]) * 100
    except ZeroDivisionError:
        percentage_correct = 0
    text_to_display = f"Game Over! You scored {session['score']} out of {session['rounds_counter']} ({percentage_correct:.2f}%)"

    return render_template("game_over.html", text=text_to_display)


@app.route("/reset")
def reset():
    session["score"] = 0
    session["rounds_counter"] = 0

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
