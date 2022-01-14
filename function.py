from extension import *

db = SQLAlchemy(app)


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    dex = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(80), nullable=False)

    def json(self):
        return {"id": self.id, "name": self.name,
                "dex": self.dex, "type": self.type}

    def add_pokemon(_name, _dex, _type):
        new_pokemon = Pokemon(name=_name, dex=_dex, type=_type)
        db.session.add(new_pokemon)
        db.session.commit()

    def get_all_pokemon():
        return [Pokemon.json(pokemon) for pokemon in Pokemon.query.all()]

    def get_pokemon(_id):
        return [Pokemon.json(Pokemon.query.filter_by(id=_id).first())]

    def update_pokemon(_id, _name, _dex, _type):
        pokemon_to_update = Pokemon.query.filter_by(id=_id).first()
        pokemon_to_update.name = _name
        pokemon_to_update.dex = _dex
        pokemon_to_update.type = _type
        db.session.commit()

    def delete_pokemon(_id):
        Pokemon.query.filter_by(id=_id).delete()
        db.session.commit()
