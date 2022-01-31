from function import *


@app.route("/pokedex", methods=["GET"])
def get_pokemon():
    return jsonify(Pokemon.get_all_pokemon())


@app.route("/pokedex/<int:id>", methods=["GET"])
def get_pokemon_by_id(id):
    return_value = Pokemon.get_pokemon(id)
    return jsonify(return_value)


@app.route("/pokedex", methods=["POST"])
def add_pokemon():
    request_data = request.get_json()
    Pokemon.add_pokemon(request_data["name"], request_data["dex"],
                        request_data["type"])
    response = Response("Pokemon Added To The List", 201, mimetype="application/json")
    return response


@app.route("/pokedex/<int:id>", methods=["DELETE"])
def remove_pokemon(id):
    Pokemon.delete_pokemon(id)
    response = Response("Pokemon Deleted", status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(debug=True)
