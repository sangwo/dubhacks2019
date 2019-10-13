from flask import Flask, render_template, request, jsonify, json
import requests
app = Flask(__name__)

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
recipe_api_key_file = os.path.join(THIS_FOLDER, 'recipe_api_key.txt')

RECIPE_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"

@app.route('/')
def main():
  return render_template('index2.html') # change it to index.html

@app.route('/recipes', methods=['POST'])
def show_recipes():
  ingredients = request.form['ingredients']
  ingredients = ingredients.encode("ascii")
  return render_template('results2.html', ingredients=ingredients) # change it to results.html

@app.route('/search')
def search_recipes():
  ingredients = request.args.get('ingredients')

  file = open(recipe_api_key_file, "r")
  recipe_api_key_json = file.read()
  recipe_api_key = json.loads(recipe_api_key_json)['api_key']
  file.close()

  url = RECIPE_API_URL + "?apiKey={}".format(recipe_api_key)

  headers = {
    "Content-Type": "application/json"  
  }

  params = {
    "ingredients": ingredients,
    "number": 1
  }

  response = requests.get(url, headers=headers, params=params)
  return jsonify(response.content)
