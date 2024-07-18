from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/play_round', methods=['GET', 'POST'])
def play_round():
    selected_option = request.args.get('selected_option')
    current_score = request.args.get('current_score')
    print(f"Selected Option: {selected_option}")
    print(f"Current Score: {current_score}")
    if current_score is None:
        current_score = 0

    # Example options, replace with your actual logic
    options = ["Fisch 1", "Fisch 2", "Fisch 3", "Finte"]
    random.shuffle(options)

    # Assuming you want to do something with selected_option and current_score here
    
    
    score = str(int(current_score) + 1)

    return render_template('index.html', score=score, options=options)

if __name__ == '__main__':
    app.run(debug=True)