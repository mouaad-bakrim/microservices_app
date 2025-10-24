from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    quantite = db.Column(db.Integer, nullable=False, default=0)
    prix_unitaire = db.Column(db.Float, nullable=False, default=0.0)

@app.route('/produits', methods=['GET'])
def get_produits():
    produits = Produit.query.all()
    return jsonify([
        {"id": p.id, "nom": p.nom, "quantite": p.quantite, "prix": p.prix_unitaire} 
        for p in produits
    ])

@app.route('/update_stock', methods=['POST'])
def update_stock():
    data = request.get_json()
    if not data or 'id' not in data or 'quantite' not in data:
        return jsonify({"error": "Données invalides"}), 400

    produit = Produit.query.get(data['id'])
    if not produit:
        return jsonify({"error": "Produit introuvable"}), 404

    if produit.quantite < data['quantite']:
        return jsonify({"error": "Stock insuffisant"}), 400

    produit.quantite -= data['quantite']
    db.session.commit()
    return jsonify({"message": "Stock mis à jour", "produit": {
        "id": produit.id,
        "nom": produit.nom,
        "quantite": produit.quantite,
        "prix": produit.prix_unitaire
    }})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée la base et les tables si elles n'existent pas

    app.run(host='0.0.0.0', port=8000)
