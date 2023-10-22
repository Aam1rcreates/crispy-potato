from flask_cors import CORS
from serpapi import GoogleSearch
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/get-data", methods=["POST"])
def get_data():
  params = {
    "q": request.get_json()["search_txt"],
    "location": "Delhi, India",
    "hl": "en",
    "gl": "us",
    "api_key": "API_Key" # Get your api key from serpapi and replace here
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  try:
    if 'shopping_results' not in results:
      return jsonify({
        "success": False,
        "message": f"No shopping ads found for {params['q']}."
      })
    else:
      res = {
        "title": results['shopping_results'][0]['title'],
        "price": results['shopping_results'][0]['price'],
        "link": results['shopping_results'][0]['link'],
        "image": results['shopping_results'][0]['thumbnail']
      }
      return jsonify({
        "success": True,
        "data": {
          "title": res["title"],
          "price": res["price"],
          "link": res["link"],
          "image": res["image"]
        }
      })
  except Exception as e:
    return jsonify({
      "error": True,
      "message": "Something went wrong!"
    })

if __name__ == '__main__':
    app.run(debug=True)