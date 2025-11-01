from flask import Flask, render_template, request, send_file
import json

app = Flask(__name__)  # ✅ This line defines 'app'

@app.route('/')
def home():
    search_query = request.args.get('search', '').lower()
    with open('recipes.json') as f:
        recipes = json.load(f)
    if search_query:
        recipes = [r for r in recipes if search_query in r['name'].lower()]
    return render_template('food.html', recipes=recipes)

@app.route('/download')
def download():
    return send_file('recipes.json', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)