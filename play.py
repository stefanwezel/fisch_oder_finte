from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
)
import random
from src.commons import pickle_to_list


app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/")
def index():
    if "score" not in session:
        session["score"] = 0
    if "rounds_counter" not in session:
        session["rounds_counter"] = 0

    real_fishes = pickle_to_list("data/real_fish.pickle")
    made_up_fishes = pickle_to_list("data/made_up_fish.pickle")

    real_options = random.sample(real_fishes, k=3)
    finte = random.sample(made_up_fishes, k=1)[0]

    options = real_options + [finte]
    random.shuffle(options)

    correct_index = options.index(finte)
    correct_option = options[correct_index]
    session["correct_option"] = correct_option

    return render_template("index.html", options=options, score=session["score"])


@app.route("/submit", methods=["POST"])
def submit():
    session["rounds_counter"] += 1
    selected_option = request.form.get("option")

    if not selected_option:
        flash("Please select an option.")
        return redirect("/")

    if selected_option == session.get("correct_option"):
        session["score"] += 1
        flash(f"Correct! {random.choice(['🐟', '🐠', '🐡', '🦈'])}")
    else:
        flash(f"Incorrect! {random.choice(['🎣', '🍣', '🍤'])}")

    print(f"Selected option: {selected_option}, Score: {session['score']}")

    return redirect("/")


@app.route("/end_game", methods=["GET", "POST"])
def end_game():
    percentage_correct = (session["score"] / session["rounds_counter"]) * 100
    text_to_display = f"Game Over! You scored {session['score']} out of {session['rounds_counter']} ({percentage_correct:.2f}%)"

    return render_template("game_over.html", text=text_to_display)


@app.route("/reset")
def reset():
    session["score"] = 0
    session["rounds_counter"] = 0

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
